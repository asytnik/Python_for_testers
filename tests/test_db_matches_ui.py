# -*- coding: utf-8 -*-
from model.group import Group
from model.param import Param
import re


def test_group_list(apl, db):
    ui_list = apl.group.get_group_info()
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    db_list = list(map(clean, db.get_group_info()))
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)


def test_contact_ui_db_same(apl, db):
    ui_cont_info = apl.contact.get_contact_info()
    db_cont_info = db.get_contact_info()
    assert ui_cont_info.firstname == db_cont_info.firstname

    #assert sorted(ui_cont_info, key=Param.max_or_id) == sorted(db_cont_info, key=Param.max_or_id)

def clear(s):
    return re.sub("[ ]", "", s)

