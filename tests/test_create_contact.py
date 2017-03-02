# -*- coding: utf-8 -*-
from model.param import Param
import pytest
import random
import string


def random_name(prefix, maxlen):
    symbols = string.ascii_letters + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_address(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + "-" + "." + "," + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_phone_digits(prefix, maxlen):
    symbols = string.digits + "()"*10 + "("*5 + ")"*5 + "-"*5 + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_email_address(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + "@" + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Param(lastname="", firstname="", address="", homephone="", mobilephone="", workphone="",
                  email="", email2="", email3="")] + [
    Param(lastname=random_name("lastname",15), firstname=random_name("firstname",15),
          address=random_address("address",50), homephone=random_phone_digits("+",15),
          mobilephone=random_phone_digits("+",15), workphone=random_phone_digits("workphone",15),
          email=random_email_address("email",25), email2=random_email_address("email2",25), email3=random_email_address("email3",25))
    for i in range(5)]

@pytest.mark.parametrize("param", testdata, ids=[repr(x) for x in testdata])
def test_create_contact(apl,param):
    old_contacts = apl.contact.get_contact_list()
    apl.contact.new_contact_creation(param)
    new_contacts = apl.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(param)
    assert sorted(old_contacts, key=Param.max_or_id) == sorted(new_contacts, key=Param.max_or_id)


#def test_with_empty_spaces(apl):
#    old_contacts = apl.contact.get_contact_list()
#    contact = Param(lastname="", firstname="", address="",homephone="", mobilephone="",
#                    workphone="", email="", email2="", email3="")
#    apl.contact.new_contact_creation(contact)
#    new_contacts = apl.contact.get_contact_list()
#    assert len(old_contacts) + 1 == len(new_contacts)
#    old_contacts.append(contact)
#    assert sorted(old_contacts, key=Param.max_or_id) == sorted(new_contacts, key=Param.max_or_id)