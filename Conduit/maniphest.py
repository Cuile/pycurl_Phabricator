#!/usr/bin/python
# -*- coding: utf-8 -*-


def search(ph, data={}):
    return ph.call_method('maniphest.search', data)


def search_by_project_name(ph, project_name):
    parameters = {'queryKey': 'all', 'constraints': {"projects": [project_name]}}
    return search(ph, parameters)
