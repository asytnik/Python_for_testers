# -*- coding: utf-8 -*-
from fixture.orm import ORMFixture
from model.group import Group
# import pymysql.cursors

db=ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

# connection = mysql.connector.connect(host="127.0.0.1", database="addressbook", user="root", password="")
# connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")

try:
    l = db.get_contacts_not_in_group(Group(id='503'))
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
