__author__ = 'jarrah'
import peewee as pw
from playhouse.shortcuts import model_to_dict


_db = pw.MySQLDatabase(database="test", host="10.10.81.163", port=3306, user="bluetest", passwd="123456")


class MySQLModel(pw.Model):
    """A base model that will use our MySQL database"""

    class Meta:
        database = _db

    def to_json_exclude(self, *args):
        return model_to_dict(self, exclude=args)

def get_db():
    return _db