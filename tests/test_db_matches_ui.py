# -*- coding: utf-8 -*-
from model.group import Group
from model.param import Param
import re

def test_group_list(apl, db):
    ui_list = apl.group.get_group_list()
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    db_list = map(clean, db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)


def test_contact_list(apl, db):
    ui_cont_list = apl.contact.get_contact_list()
    cont_info_from_db = db.get_contact_list()
    merge_db_cont_list = merge_all_db_cont_info(cont_info_from_db)
    assert sorted(ui_cont_list, key=Param.max_or_id) == sorted(merge_db_cont_list, key=Param.max_or_id)

def clear(s):
    return re.sub("[ ]", "", s)

def merge_all_db_cont_info(param):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                   filter(lambda x: x is not None,
                                          [param.lastname, param.firstname,param.address,
                                                param.all_db_cont_phones, param.all_db_cont_email]))))