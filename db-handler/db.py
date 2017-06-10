#!/usr/bin/env python3
# coding=utf-8

import codecs
import os
from symbol import decorator

from peewee import *
from simplejson import load, dump

MYSQL_HOST = '127.0.0.1'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWD = 'root'
MYSQL_DB = 'zhaopin'
MYSQL_USRE_TABLE_NAME = 'user'

# ---------------------建立虚拟疾病的属性，即添加icon、iconColor字段到tag_property中---2----------------
user = None
resume = None

dir_path_algo_mail_content = os.path.dirname(os.path.realpath(__file__))
db_hb = MySQLDatabase(MYSQL_DB, host=MYSQL_HOST, port=3306, user=MYSQL_USER, passwd=MYSQL_PASSWD)


class BaseModel(Model):
    def __str__(self):
        r = {}
        for k in self._data.keys():
            try:
                r[k] = str(getattr(self, k))
            except:
                r[k] = dump(getattr(self, k))
        return str(r)


class User(BaseModel):
    id = PrimaryKeyField()
    email = CharField()
    gender = IntegerField()
    img_url = CharField()
    name = CharField()
    nike_name = CharField()
    password = CharField()
    phone = CharField()

    class Meta:
        database = db_hb
        db_table = MYSQL_USRE_TABLE_NAME



def create_user_to_db():

    json_file = dir_path_algo_mail_content + '/user.json'
    user_info_list = load(codecs.open(json_file, "r", "utf-8"))
    for user_info in user_info_list["userList"]:
        # print(user_info_list[user_info])
        create_user_object(user_info)


def create_user_object(user_info):
    user = User()
    user.email = user_info.get("email")
    user.gender = user_info.get("gender")
    user.img_url = user_info.get("imageUrl")
    user.name = user_info.get("name")
    user.nike_name = user_info.get("nikeName")
    user.password = user_info.get("password")
    user.phone = user_info.get("phone")

    user.save()
    print("add success")

if __name__ == "__main__":
    create_user_to_db()
