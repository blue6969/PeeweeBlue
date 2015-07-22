__author__ = 'jarrah'

'''-------base define start-------'''

'''code define'''
CODE_ERROR = -1
CODE_SUCCESS = 1000

'''response keys'''
KEY_RESPONSE_CODE = 'code'
KEY_RESPONSE_MSG = 'msg'
KEY_RESPONSE_EXTRA = 'extra'

'''response msg'''
MSG_OK = 'ok'
MSG_ERROR = 'error'

'''-------base define end-------'''

'user'
# CODE_EXISTED_USER = 1002
# CODE_PASSWORD_ERROR = 1004
# CODE_USER_NOT_EXIST = 1006
# CODE_USER_MSG_CODE_ERROR = 1008

class UserCode:
    EXISTED_USER = 1002
    PASSWORD_ERROR = 1004
    USER_NOT_EXIST = 1006
    USER_MSG_CODE_ERROR = 1008

    def __init__(self):
        pass

class UserKey:
    JSON_PHONE = 'phone'
    JSON_PASSWORD = 'password'
    JSON_NICK = 'nick'

    ARG_USER_ID = 'uid'

    SQL_TS = 'ts'

    def __init__(self):
        pass

class MomentKey:

    ARG_CIRCLE_ID = 'circle_id'

    JSON_CONTENT = 'content'
    JSON_TITLE = 'title'
    JSON_DATA = 'data'

    def __init__(self):
        pass
