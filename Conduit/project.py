#!/usr/bin/python
# -*- coding: utf-8 -*-


def search(ph, data={}):
    return ph.call_method('project.search', data)


def search_by_name(ph, name):
    parameters = {'queryKey': 'all', 'constraints': {'name': name}}
    return search(ph, parameters)
