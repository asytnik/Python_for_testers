# -*- coding: utf-8 -*-
from model.group import Group

def test_create_group(apl):
    apl.group.creation_group(Group(name="groups", header="jjhjhvbv", footer="gfjgyfghvjgg"))

def test_create_empty_group(apl):
    apl.group.creation_group(Group(name="", header="", footer=""))