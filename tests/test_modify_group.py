# -*- coding: utf-8 -*-
from model.group import Group

def test_modify_fill_group_name(apl):
    if apl.group.check_fill_form() > 0:
        apl.group.clean_field_form()
    apl.group.edit_first_group(Group(name="ggigigiu"))


# def test_modify_empty_group_name(apl):
    #if apl.group.check_fill_form() == 0:
        #apl.group.fill_group_form(Group(name="jhfowhowiotest"))
    #apl.group.clean_field_form()
