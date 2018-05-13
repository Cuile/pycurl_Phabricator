#!/usr/bin/python
# -*- coding: utf-8 -*-


def search(ph, data={}):
    return ph.call_method('maniphest.search', data)
