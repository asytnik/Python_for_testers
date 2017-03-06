# -*- coding: utf-8 -*-
from model.group import Group
import random

def test_delete_some_group(apl, db, check_ui):
    if len (db.get_group_list()) == 0:
        apl.group.creation_group(Group(name="New test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    apl.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    assert old_groups == new_groups
    new_groups = map(clean, db.get_group_list())
    if check_ui:
        # new_groups = map(clean, db.get_group_list()) -- also can insert here --
        assert sorted(new_groups, key=Group.id_or_max) == sorted(apl.group.get_group_list(), key=Group.id_or_max)
