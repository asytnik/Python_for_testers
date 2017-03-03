# -*- coding: utf-8 -*-
from model.param import Param
import random
import string
import os.path
import json
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

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
    for i in range(n)]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))

