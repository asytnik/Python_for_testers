# -*- coding: utf-8 -*-
from model.group import Group
from model.param import Param


def test_group_list(apl, db):
    ui_list = apl.group.get_group_list()
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    db_list = map(clean, db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)


def test_contact_list(apl, db):
    ui_cont_list = apl.contact.get_contact_list()
    def clean(param):
        param = list(filter(lambda x: x != "",
                        map(lambda x: clean(x),
                              [param.id, param.lastname, param.firstname,  param.address,
                                    param.all_db_cont_phones, param.all_db_cont_email])))
        return param
    db_cont_list = map(clean, db.get_contact_list())
    assert sorted(ui_cont_list, key=Param.max_or_id) == sorted(db_cont_list, key=Param.max_or_id)
