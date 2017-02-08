# -*- coding: utf-8 -*-

def test_del_contact(apl):
    apl.session.login_into(username="admin", password="secret")
    apl.contact.del_contact()
