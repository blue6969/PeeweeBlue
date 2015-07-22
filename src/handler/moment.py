# coding: utf-8
import time
import tornado
from tornado.escape import json_decode, json_encode
from playhouse.shortcuts import model_to_dict
from src.model.blue import Moment, Image
from src.tools.base import BaseHandler
from src.tools.packer import gen_link_obj, dump_list_view_pack
from src.tools import path_util as path
from src.tools.constant import MomentKey


__author__ = 'jarrah'

UPLOAD_IMAGE_PARAMS = ['image0', 'image1', 'image2', 'image3', 'image4', 'image5', 'image6', 'image7', 'image8']


def url_spec(**kwargs):
    return [
        (r'/moment', MomentHandler, kwargs),
    ]

IMG_DIR = path.img_uploads_path

class MomentHandler(BaseHandler):

    def get(self, *args, **kwargs):
        index = self.get_index()
        moment_items = self.get_moment_items(index=index)
        next_link = gen_link_obj("next", self.settings['HOST_MOMENT'] + "?index=%d" % (int(index) + 1))
        items = dump_list_view_pack(moment_items, next_link)
        self.write(items)

    def get_moment_items(self, index=0):
        rows = Moment.select().paginate(index, 1)
        items = list()
        for row in rows:
            items.append(model_to_dict(row))
        return items

    '''multipart '''

    def post(self, *args, **kwargs):
        circle_id = self.get_arg(MomentKey.ARG_CIRCLE_ID)
        user = self.get_user_info()

        moment_data = self.get_moment_data()
        if not moment_data:
            raise tornado.web.MissingArgumentError('missing args')

        images = ""
        for param in UPLOAD_IMAGE_PARAMS:
            file_name = self.save_image(param)
            if file_name is None:
                break
            # image_id = service.insert_post_image(user['uid'], file_name)
            Image.insert(ts=int(time.time()), path=file_name).execute()
            image = Image.get(Image.path == file_name)

            images += str(image.id)
            images += '|'

        images = images[:-1]

        Moment.insert(
            ts=int(time.time()),
            post_user=user['uid'],
            circle=circle_id,
            content=moment_data[MomentKey.JSON_CONTENT],
            title=moment_data[MomentKey.JSON_TITLE],
            image=images
        ).execute()

        self.write(self.ok_pack())

    def get_moment_data(self):
        data = self.get_argument(MomentKey.JSON_DATA, None)
        if data is None:
            return None
        data = json_decode(data)
        if MomentKey.JSON_TITLE in data and MomentKey.JSON_CONTENT in data:
            return data
        else:
            return None
