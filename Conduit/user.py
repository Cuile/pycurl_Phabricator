#!/usr/bin/python
# -*- coding: utf-8 -*-


def whoami(ph, data={}):
    return ph.call_method('user.whoami', data)


def search(ph, data={}):
    return ph.call_method('user.search', data)


def search_by_email(ph, email):
    parameters = {'queryKey': 'all', 'constraints': {'usernames': [email.split('@')[0]]}}
    return search(ph, parameters)
