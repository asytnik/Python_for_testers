# -*- coding: utf-8 -*-

from model.param import Param

def test_create_contact(apl):
    old_contacts = apl.contact.get_contact_list()
    contact = Param(lastname="petrov", firstname="petr")
    apl.contact.new_contact_creation(contact)
    new_contacts = apl.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Param.id_lstnm_fstnm) == sorted(new_contacts, key=Param.id_lstnm_fstnm)



#def test_with_empty_spaces(apl):
#    old_contacts = apl.contact.get_contact_list()
#    apl.contact.empty_spaces(Param(firstname="empty1", lastname="empty2"))
#    new_contacts = apl.contact.get_contact_list()
#    assert len(old_contacts) + 1 == len(new_contacts)


