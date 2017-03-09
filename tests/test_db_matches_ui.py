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
    def clear(param):
        cont = list(filter(lambda x: x != "",
                           map(lambda x: clear(x),
                               [param.id, param.lastname, param.firstname,  param.address,
                                      param.homephone, param.mobilephone, param.workphone])))
        return cont

    db_cont_list = (clear, db.get_contact_list)
    # db_cont_list = list(filter(clear, db.get_contact_list()))
    assert sorted(ui_cont_list, key=Param.max_or_id) == sorted(db_cont_list, key=Param.max_or_id)
