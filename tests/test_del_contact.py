# -*- coding: utf-8 -*-

def test_del_contact(apl):
    apl.sescontact.login_into(username="admin", password="secret")
    apl.sescontact.del_contact()
