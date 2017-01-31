# -*- coding: utf-8 -*-
import pytest
from fixture.aplicanter import Aplicant

@pytest.fixture
def apl(request):
    fixture =  Aplicant()
    request.addfinalizer(fixture.destroy)
    return fixture