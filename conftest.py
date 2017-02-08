# -*- coding: utf-8 -*-
import pytest
from fixture.aplicanter import Aplicant

fixture = None

@pytest.fixture
def apl(request):
    global fixture
    if fixture is None:
        fixture = Aplicant()
        fixture.session.login_into(username="admin", password="secret")
    else:
        if not fixture.is_valid:
            fixture = Aplicant()
            fixture.session.login_into(username="admin", password="secret")
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture