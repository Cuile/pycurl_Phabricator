#!/usr/bin/python
# -*- coding: utf-8 -*-

import Conduit
import json
from jsonpath import jsonpath

ph = Conduit.Conduit()
ph.set_url("http://ph.feinno.com/api/")
ph.set_token("api-vxzwb2kfzapq63il246w2rkv64qb")

phps = Conduit.project.search()
phps.parameters['constraints']['name'] = '和飞信_运营平台'
phps.parameters['constraints']['colors'] = ['blue', 'red']
# phps.parameters = {"constraints": {"name": "和飞信_运营平台"}}

# print(phps.parameters)
# print(ph.call_method(phps))
print(jsonpath(phps.parameters, '$..colors', result_type='VALUE'))
print(jsonpath(phps.parameters, '$..colors', result_type='IPATH'))
print(jsonpath(phps.parameters, '$..colors', result_type='PATH'))

exit()

# ph.set_token('')
# ph.get_userPHID_for_username('cuile')
# projectPHID = ph.get_projectPHID_for_name('')
# task_PHIDs = ph.get_taskPHIDs_for_projectPHID(projectPHID)
# print(task_PHIDs)
