# -*- coding: utf-8 -*-
import pytest
from fixture.aplicanter import Aplicant
from model.param import Param, Phone, Email


@pytest.fixture
def apl(request):
    fixture=Aplicant()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_new_contact(apl):
    apl.sescontact.login_into(username="admin", password="secret")
    apl.fillcredentials.fill_name_occupation_address(Param(name="ivan", lastname="ivanov", nickname="balda", title="worker", company="church",
                                          address="1230 Avenue X, Brooklyn, NY"))
    apl.opensession.fill_phone_number(Phone(home="+1 113 456 987 654", mobile="+2 225 456 874 986", work="+2 325 685 965 784"))
    apl.opensession.fill_e_mail_DOB(Email(email1="balda@mail.ru", email2="pop2@mail.ru", dob="1990"))
    apl.opensession.fill_second_address(address2="4554 Neptune Av., Brooklyn,NY")

def test_with_empty_spaces(apl):
    apl.sescontact.login_into(username="admin", password="secret")
    apl.fillcredentials.fill_name_occupation_address(Param(name="ivan", lastname="ivanov", nickname="balda", title="", company="",
                                          address=""))
    apl.opensession.fill_phone_number(Phone(home="+1 113 456 987 654", mobile="+2 225 456 874 986", work=""))
    apl.opensession.fill_e_mail_DOB(Email(email1="balda@mail.ru", email2="", dob="1990"))
    apl.opensession.fill_second_address(address2="")

