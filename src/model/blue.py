__author__ = 'jarrah'

from peewee import *

from pw import MySQLModel, get_db


class Image(MySQLModel):
    id = PrimaryKeyField()
    path = CharField(unique=True)
    ts = BigIntegerField()


class User(MySQLModel):
    id = PrimaryKeyField()
    phone = CharField(unique=True)
    email = CharField(null=True)
    nick = CharField()
    bind_app_id = IntegerField(null=True, unique=True)
    ts = BigIntegerField()
    password = CharField()
    portrait = ForeignKeyField(Image, related_name='portrait_image', null=True)


class Circle(MySQLModel):
    id = PrimaryKeyField()
    title = CharField()
    slogan = CharField()
    followers = TextField()
    hot_count = IntegerField()
    image = ForeignKeyField(Image, related_name='circle_image')


class Moment(MySQLModel):
    id = PrimaryKeyField()
    content = CharField()
    title = CharField()
    image = TextField()
    post_user = ForeignKeyField(User, related_name='moment_user', null=True)
    ts = BigIntegerField()
    circle = ForeignKeyField(Circle, related_name='moment_circle', null=True)

class Comment(MySQLModel):
    id = PrimaryKeyField()
    ts = BigIntegerField()
    content = CharField()
    post_user = ForeignKeyField(User, related_name='comment_user')
    reply_type = IntegerField()
    image = ForeignKeyField(Image, related_name='comment_image', null=True)
    moment = ForeignKeyField(Moment, related_name="comment_moment")

def create():
    get_db().create_tables([User, Image, Moment, Circle, Comment], safe=True)