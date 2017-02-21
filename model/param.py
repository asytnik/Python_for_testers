# -*- coding: utf-8 -*-

from sys import maxsize

class Param:

    def __init__(self, lastname=None, firstname=None,  nickname=None, title=None, company=None, address=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.lastname, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.lastname == other.lastname and self.firstname == other.firstname

    def max_or_id(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize