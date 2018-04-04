#!/usr/bin/python
# -*- coding: utf-8 -*-
import Conduit

ph = Conduit._base()
ph.set_url("http://ph.feinno.com/api/")
ph.set_token("api-vxzwb2kfzapq63il246w2rkv64qb")
Conduit.project(ph).search()
print(Conduit.user(ph).whoami())

exit()

# ph.set_token('')
# ph.get_userPHID_for_username('cuile')
# projectPHID = ph.get_projectPHID_for_name('')
# task_PHIDs = ph.get_taskPHIDs_for_projectPHID(projectPHID)
# print(task_PHIDs)
