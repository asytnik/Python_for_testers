# -*- coding: utf-8 -*-
from model.group import Group

def test_modify_first_group_name(apl):
    apl.group.check_empty_form()
    apl.group.edit_first_group(Group(name="Big boss"))

#def test_modify_fill_group_name(apl):
#   if apl.group.editor_group_name() is not None:
#       apl.group.checking_forms(Group(name="Old test"))
