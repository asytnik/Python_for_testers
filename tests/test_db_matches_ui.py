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
    for lastname in db_cont_info, ui_cont_info:
        for firstname in db_cont_info, ui_cont_info:
            for address in db_cont_info, ui_cont_info:
                return (lastname,firstname,address)
#    for firstname in db_cont_info, ui_cont_info:
#        return (firstname)
#    for address in db_cont_info, ui_cont_info:
#        return (address)
    assert sorted(db_cont_info.lastname, key=Param.max_or_id) == sorted(ui_cont_info.lastname, key=Param.max_or_id)
    assert sorted(db_cont_info.firstname, key=Param.max_or_id) == sorted(ui_cont_info.firstname, key=Param.max_or_id)
    assert sorted(db_cont_info.address, key=Param.max_or_id) == sorted(ui_cont_info.address, key=Param.max_or_id)


def clear(s):
    return re.sub("[ ]", "", s)

