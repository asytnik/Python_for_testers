# -*- coding: utf-8 -*-
from model.group import Group

def test_edit_group_name(apl):
    apl.group.edit_first_group(Group(name="zomby"))

def test_edit_group_header(apl):
    apl.group.edit_first_group(Group(header="fregat"))

