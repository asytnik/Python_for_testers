# -*- coding: utf-8 -*-
from model.group import Group

def test_edit_group(apl):
    apl.session.login_into(username="admin", password="secret")
    apl.group.edit_group(Group(name="zomby", header="fregat", footer="columbus"))
