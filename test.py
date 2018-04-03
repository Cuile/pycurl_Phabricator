#!/usr/bin/python
# -*- coding: utf-8 -*-
from Conduit import *

ph = base()
ph.set_url("http://ph.feinno.com/api/")
project(ph).search()


# ph.set_token('')
# ph.get_userPHID_for_username('cuile')
# projectPHID = ph.get_projectPHID_for_name('')
# task_PHIDs = ph.get_taskPHIDs_for_projectPHID(projectPHID)
# print(task_PHIDs)
