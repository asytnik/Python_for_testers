# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange
import random
import re


def test_modify_group_by_index(apl, db):
    if len (db.get_group_info()) == 0:
        apl.group.creation_group(Group(name="New group", header="Old header", footer="Old footer"))
    old_groups = apl.group.get_group_info()
    index = randrange(len(old_groups))
    group = Group(name="Old group", header="Old header", footer="Old footer")
    group.id = old_groups[index].id
    apl.group.edit_group_by_index(index, group)
    new_groups = db.get_group_info()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    new_groups = list(map(clean, db.get_group_info()))
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

    #def clean(group):
     #   return Group(id=group.id, name=group.name.strip())
    #db_list = list(map(clean, db.get_group_info()))

def test_modify_group_by_id(apl, db, check_ui):
    if len(db.get_group_info()) == 0:
        apl.group.creation_group(Group(name="New group", header="New header", footer="New footer"))
    old_groups = db.get_group_info()
    group = random.choice(old_groups)
    new_group_data = Group(name="Bingo_lotto", header="Strike_header", footer="Ball_footer")
    apl.group.edit_group_by_id(group.id, new_group_data)
    new_groups = db.get_group_info()
    assert len(old_groups) == len(new_groups)
    #new_groups = map(clean, db.get_group_info())  # -- also can insert here --
    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)
    if check_ui:
        new_groups = map(clean, db.get_group_info())  # -- also can insert here --
        assert sorted(new_groups, key=Group.id_or_max) == sorted(apl.group.get_group_info(), key=Group.id_or_max)


def clean(s):
    return re.sub("[ ]", "", s)
#def clean(group):
     #   return Group(id=group.id, name=group.name.strip())


def test_modify_fill_group_name(apl):
    if apl.group.counter_group() == 0:
        apl.group.creation_group(Group(name="New group", header="Old header", footer="Old footer"))
    old_groups = apl.group.get_group_info()
    index = randrange(len(old_groups))
    group=Group(name="Old group", header="Old header", footer="Old footer")
    group.id = old_groups[index].id
    apl.group.edit_group_by_index(index, group)
    new_groups = apl.group.get_group_info()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
