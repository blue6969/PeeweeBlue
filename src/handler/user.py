import time

from src.tools.base import BaseHandler
from src.model.blue import User
from src.tools.constant import UserCode, UserKey

__author__ = 'jarrah'


def url_spec(**kwargs):
    return [(r'/user/login', LoginHandler, kwargs), (r'/user', UserHandler, kwargs), ]


class LoginHandler(BaseHandler):
    def post(self, *args, **kwargs):
        json = self.get_post_json(UserKey.JSON_PHONE, UserKey.JSON_PASSWORD)
        self.query_user(json)

    def query_user(self, json):

        try:
            user = User.get(User.phone == json[UserKey.JSON_PHONE])
        except:
            user = None

        if user is None:
            self.write(self.make_response_pack('user does not exist', UserCode.USER_NOT_EXIST))
            return

        if json[UserKey.JSON_PASSWORD] != user.password:
            self.write(self.make_response_pack('password error', UserCode.PASSWORD_ERROR))
            return

        if json[UserKey.JSON_PASSWORD] == user.password and json[UserKey.JSON_PHONE] == user.phone:
            token = self.token_encode(user.id, User.phone)
            self.set_secure_token(token)
            user = user.to_json_exclude(User.bind_app_id, User.id, User.password, User.ts, User.email)
            self.write(self.make_response_pack('login success', user=user))
            return


class UserHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.get_user_info()
        user_id = self.get_arg(UserKey.ARG_USER_ID)
        user = User.get(User.id == user_id)
        self.write(self.make_response_pack(
            **user.to_json_exclude(User.bind_app_id, User.id, User.password, User.ts, User.email)))

    def post(self, *args, **kwargs):
        json = self.get_post_json(UserKey.JSON_NICK, UserKey.JSON_PASSWORD, UserKey.JSON_PHONE)
        json[UserKey.SQL_TS] = int(time.time())

        if self.get_user_safe(json):
            self.write(self.make_response_pack(msg='user existed!', code=UserCode.EXISTED_USER))
        else:
            User.insert(**json).execute()
            self.write(json)

    def get_user_safe(self, json):
        try:
            user = User.get(User.phone == json[UserKey.JSON_PHONE])
        except:
            user = None
        return user
