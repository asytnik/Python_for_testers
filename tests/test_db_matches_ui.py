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
    assert len(ui_cont_info) == len(db_cont_info)
    ui_info = []
    for ui in ui_cont_info:
        ui_info.append(Param(id=ui.id, lastname=ui.lastname, firstname=ui.firstname, address=ui.address,
                             all_phones_from_home_page=ui.all_phones_from_home_page, all_email_from_home_page=ui.all_email_from_home_page))
    db_info = []
    for db in  db_cont_info:
        db_info.append(Param(id=db.id, lastname=db.lastname, firstname=db.firstname, address=db.address,
                             all_db_cont_phones=db.all_db_cont_phones, all_db_cont_email=db.all_db_cont_email))
    def clean_string(str):
        return re.sub("\s+", " ", str.strip())
    def clean_param(param):
            return Param(id=param.id, lastname=clean_string(param.lastname), firstname=clean_string(param.firstname), address=clean_string(param.address))
    db_info = list(map(clean_param,db_cont_info))
    assert sorted (db_info, key=Param.max_or_id) == sorted (ui_info, key=Param.max_or_id)


def test_data_ui_db_match(apl, db):
    ui_list = apl.contact.get_contact_info()
    db_list = db.get_contact_info()
    assert len(sorted(ui_list, key=Param.max_or_id)) == len(sorted(db_list, key=Param.max_or_id))
    db_object = ["firstname", "lastname", "address"]  #all_db_cont_phones=[home, mobile, work], all_db_cont_email=[email, email2, email3])email=[email, email2, email3])
    ui_object = ["firstname", "lastname", "address"] # all_phones_from_home_page=(all_phones), all_email_from_home_page=(all_email)))
    for i in range(len(db_list)):
        db_object = db_list[i]
        ui_object = ui_list[i]
    assert db_object.firstname == ui_object.firstname
    #assert db_object.lastname == ui_object.lastname
    #assert db_object.address == ui_object.address




#def clean(s):
  #  return re.sub("[ ]", "", s)
    #return compile("[  ]", db_cont_info).sub("", s)

# -- re expressions from A.Barantsev --
# def clean_string(str):
#    return re.sub("\s+", " ", str.strip())

#def clean_group(group):
#    return Group(id=group.id, name=clean_string(group.name),header=clean_string(group.header), footer=clean_string(group.footer))

# ' '.join(YYY.split())
# re.sub(r'\s+', ' ', YYY)





