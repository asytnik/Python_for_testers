# -*- coding: utf-8 -*-
from model.param import Param
import random
import string

constant = [
    Param(lastname="lastname1", firstname="firstname1", address="address1", homephone="homephone1",
          mobilephone="mobilephone1", workphone="workphone1", email="email_1", email2="email2_1", email3="email3_1"),
    Param(lastname="lastname2", firstname="firstname2", address="address2", homephone="homephone2",
          mobilephone="mobilephone2", workphone="workphone2", email="email_2", email2="email2_2", email3="email3_3")
]

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
