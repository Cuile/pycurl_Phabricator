#!/usr/bin/python
# -*- coding: utf-8 -*-


def whoami(ph, data={}):
    return ph.call_method('user.whoami', data)
