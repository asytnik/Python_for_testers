# -*- coding: utf-8 -*-
import pymysql.cursors
# import mysql.connector
from model.group import Group
from model.param import Param


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password)
        # self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit = True

    def get_group_info(self):
        list =[]
        cursor = self.connection.cursor()
        # cursor = self.cursors()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list


    def get_contact_info(self):
        list2 = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, email, email2, email3 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, email, email2, email3) = row
                list2.append(Param(id=str(id), firstname=firstname, lastname=lastname, address=address,
                                   all_db_cont_phones=[home, mobile, work], all_db_cont_email=[email, email2, email3]))
        finally:
            cursor.close()
        return list2

    def destroy(self):
        self.connection.close()