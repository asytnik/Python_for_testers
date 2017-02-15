# -*- coding: utf-8 -*-
from model.group import Group

def test_modify_fill_group_name(apl):
    if apl.group.counter_group() == 0:
        apl.group.edit_first_group(Group(name="ggigigiu"))
    apl.group.delete_first_group()


