# -*- coding: utf-8 -*-
import pytest
from fixture.Application import Application
from fixture.aplicanter import Aplicant

@pytest.fixture
def app(request):
    fixture =  Application()
    request.addfinalizer(fixture.destroy)
    return fixture

@pytest.fixture
def apl(request):
    fixture =  Aplicant()
    request.addfinalizer(fixture.destroy)
    return fixture