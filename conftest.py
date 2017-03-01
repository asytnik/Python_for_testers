# -*- coding: utf-8 -*-
import pytest
from fixture.aplicanter import Aplicant

fixture = None

@pytest.fixture
def apl(request):
    global fixture
    if fixture is None:
        browser = request.config.getoption("--browser")
        base_url = request.config.getoption("--baseUrl")
        fixture = Aplicant(browser=browser, base_url=base_url)
    else:
        if not fixture.is_valid():
            fixture = Aplicant()
    fixture.session.ensure_login_into(username="admin", password="secret")
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook/")

