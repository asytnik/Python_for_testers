# -*- coding: utf-8 -*-
from fixture.orm import ORMFixture
from model.group import Group
from fixture.db import DbFixture
# import pymysql.cursors
import mysql.connector

# db=ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
db=DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")

connection = mysql.connector.connect(host="127.0.0.1", database="addressbook", user="root", password="")
# connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")

try:
    l = db.get_group_info()
    for item in l:
       print(item)
    print (len(l))
finally:
    pass # db.destroy()


#try:
  #  cursor = connection.cursor()
 #   cursor.execute("select * from group_list")
 #   for row in cursor.fetchall():
   #     print(row)
#finally:
  #  connection.close()
