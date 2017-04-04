#!/usr/bin/python
# -*- coding: utf-8 -*-
from ConduitAPI import conduit_api

ph = conduit_api()
ph.set_url('')
ph.set_token('')
# ph.get_userPHID_for_username('cuile')
projectPHID = ph.get_projectPHID_for_name('')
task_PHIDs = ph.get_taskPHIDs_for_projectPHID(projectPHID)
print(task_PHIDs)
