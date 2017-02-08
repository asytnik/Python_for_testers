# -*- coding: utf-8 -*-
import pytest
from fixture.aplicanter import Aplicant

@pytest.fixture(scope="session")
def apl(request):
    fixture =  Aplicant()
    request.addfinalizer(fixture.destroy)
    return fixture