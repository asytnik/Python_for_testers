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
    db_info = []
    for db in  db_cont_info:
        db_info.append(Param(id=db.id, lastname=db.lastname, firstname=db.firstname, address=db.address,
                             all_db_cont_phones=db.all_db_cont_phones, all_db_cont_email=db.all_db_cont_email))
    ui_info = []
    for ui in ui_cont_info:
        ui_info.append(Param(id=ui.id, lastname=ui.lastname, firstname=ui.firstname, address=ui.address,
                             all_phones_from_home_page=ui.all_phones_from_home_page, all_email_from_home_page=ui.all_email_from_home_page))
    def sub(db_info, s):
        return compile("[ ]",db_info).sub("",s,db_info)
    db_info = list(map(sub,db_cont_info))
    assert sorted (db_info, key=Param.max_or_id) == sorted (ui_info, key=Param.max_or_id)

#def clean(s):
  #  return re.sub("[ ]", "", s)
    #return compile("[  ]", db_cont_info).sub("", s)

# ' '.join(YYY.split())
# re.sub(r'\s+', ' ', YYY)





