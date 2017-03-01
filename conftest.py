# -*- coding: utf-8 -*-
import pytest
import json
import os.path
from fixture.aplicanter import Aplicant

fixture = None
target = None

@pytest.fixture
def apl(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file) as conf_obj:
            target = json.load(conf_obj)
    if fixture is None or not fixture.is_valid():
        fixture = Aplicant(browser=browser, base_url=target["baseUrl"])
    fixture.session.ensure_login_into(username=target["username"], password=target["password"])
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
    parser.addoption("--target", action="store", default="target.json")

