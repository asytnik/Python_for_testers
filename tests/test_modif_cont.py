# -*- coding: utf-8 -*-
from model.param import Param, Phone, Email

def test_modif_cont(apl):
    apl.sescontact.login_into(username="admin", password="secret")
    apl.fillcredentials.modify_name_occupation_address(Param(name="Semen", lastname="Gorbunkov", nickname="Professor",
                                                           title="Soda", company="A-A-A", address=""))
    # apl.opensession.fill_phone_number(Phone(home="+5 444 333 222 111", mobile="+7 323 979 888 666", work=""))
    # apl.opensession.fill_e_mail_DOB(Email(email1="semen_G@mail.ru"))
    # apl.opensession.fill_second_address(address2="Sunny")