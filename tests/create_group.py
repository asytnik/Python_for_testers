# -*- coding: utf-8 -*-
import pytest

from fixture.Application import Application
from model.group import Group


@pytest.fixture
def app(request):
    fixture=Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_create_group(app):
    app.login_into(username="admin", password="secret")
    app.creation_group_submit(Group(name="groups", header="jjhjhvbv", footer="gfjgyfghvjgg"))

def test_create_empty_group(app):
    app.login_into(username="admin", password="secret")
    app.creation_group_submit(Group(name="", header="", footer=""))

