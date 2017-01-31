# -*- coding: utf-8 -*-
from model.group import Group

def test_create_group(apl):
    apl.session.login_into(username="admin", password="secret")
    apl.group.creation_and_submit(Group(name="groups", header="jjhjhvbv", footer="gfjgyfghvjgg"))

def test_create_empty_group(apl):
    apl.session.login_into(username="admin", password="secret")
    apl.group.creation_and_submit(Group(name="", header="", footer=""))
