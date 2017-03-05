# -*- coding: utf-8 -*-
from model.group import Group
import random

def test_delete_some_group(apl, db):
    if len (db.get_group_list()) == 0:
        apl.group.creation_group(Group(name="New test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    apl.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    assert old_groups == new_groups
