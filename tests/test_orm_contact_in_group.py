# -*- coding: utf-8 -*-
from model.group import Group
from model.param import Param
from fixture.db import DbFixture
from fixture.orm import ORMFixture
import random

# db=ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_contact_in_group(apl,db,orm):
    if len(db.get_contact_info()) == 0:
         apl.contact.new_contact_creation(Group(name="Josef", header="vitty_header", footer="cobalt_footer"))
    all_contacts = db.get_contact_info()
    cont_in_group = orm.get_contacts_in_group(Group(id='525'))
    contact = random.choice(all_contacts)
    apl.contact.add_contact_to_group(contact.id)
    new_cont_in_group = orm.get_contacts_in_group(Group(id='525'))
    assert len(cont_in_group) + 1 == len(new_cont_in_group)


def test_del_contact_from_group(apl,db, orm):
   # if len(db.get_contact_info()) == 0:
   #      apl.contact.new_contact_creation(Group(name="Josef", header="vitty_header", footer="cobalt_footer"))
    cont_in_group = orm.get_contacts_in_group(Group(id='525'))
    contact = random.choice(cont_in_group)
    apl.contact.del_contact_from_group(contact.id)
    after_del_contacts = orm.get_contacts_in_group(Group(id='525'))
    assert len(cont_in_group) - 1 == len(after_del_contacts)

    # print (len(old_contacts))

    #cont = random.choice(old_contacts)
    #apl.contact.add_contact_to_group(cont.id)
    #id=cont.id

    #new_contacts = db.get_contact_info()
    #assert len(old_contacts) - 1 == len(new_contacts)
    #old_contacts.remove(cont)

  #  apl.contact.new_contact_creation(param)
  #  new_contacts = db.get_contact_info()
    # assert len(old_contacts) + 1 == len(new_contacts) -- can delete, no need yet --
  #  old_contacts.append(param)
   # assert sorted(old_contacts, key=Param.max_or_id) == sorted(new_contacts, key=Param.max_or_id)
