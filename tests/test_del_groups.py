# -*- coding: utf-8 -*-

def test_delete_first_group(apl):
    apl.ses_group.login_into(username="admin", password="secret")
    apl.group.delete_first_group()