from src.tools.base import BaseHandler

__author__ = 'jarrah'



def url_spec(**kwargs):
    return [
        (r'/test', TestHandler, kwargs),
    ]


class TestHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.write("hello world")