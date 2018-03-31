#!/usr/bin/python
# -*- coding: utf-8 -*-
from io import BytesIO
import urllib.parse
import json

import pycurl
import certifi


class Conduit(object):
    url = None
    token = None
    method = None
    data = {}

    def set_url(self, u):
        self.url = u
        # print("setUrl : %s" % (self.url))

    def set_token(self, t):
        self.token = t
        self.set_data({'api.token': self.token})
        # print("setToken : %s" % (self.token))

    def set_method(self, m):
        self.method = self.url + m
        # print("setMethod : %s" % (self.method))

    def set_data(self, d):
        self.data.update(d)
        # print("setData : %r" % (self.data))

    def clear_data(self):
        self.data = {}
        self.set_data({'api.token': self.token})

    def call_api(self):
        buffer = BytesIO()

        c = pycurl.Curl()

        c.setopt(c.CAINFO, certifi.where())
        # c.setopt(c.VERBOSE, True)
        c.setopt(c.POST, True)
        c.setopt(c.POSTFIELDS, urllib.parse.urlencode(self.data))
        # print(urllib.parse.urlencode(data))

        c.setopt(c.URL, self.method)
        c.setopt(c.WRITEFUNCTION, buffer.write)

        c.perform()
        c.close()

        # print("buffer : %s" % (buffer.getvalue()))
        b = buffer.getvalue().decode("utf-8")
        # print("call_api : %s" % (b))
        self.clear_data()

        return json.loads(b)

    class user(object):
        @property
        def whoami(self):
            Conduit.set_method("user.whoami")
            return Conduit.call_api()

    def get_userPHID_for_username(self, userName):
        # print('user.query'.center(40,'='))
        self.set_method("user.query")
        # print(userName)
        self.set_data({'usernames[0]': userName})
        r = self.call_api()['result'][0]['phid']
        # print("User Name is: %s, PHID is: %s" % (userName, r))
        return r

    def get_projectPHID_for_name(self, name):
        # print('project.query'.center(40,'='))
        self.set_method("project.query")
        # print(names)
        self.set_data({'names[0]': name})
        r = list(self.call_api()['result']['data'])[0]
        # print("Project Name is: %s, PHID is: %s" % (name, r))
        return r

    # QueryKey      名称      内置
    # Q841s.iJ.164  反馈      自定义
    # assigned      已指派     内置
    # authored      我创建的    内置
    # subscribed    已订阅     内置
    # open          已开启任务   内置
    # all           所有任务    内置

    # OrderKey  详情                      Columns
    # priority  优先级                     priority, subpriority, id
    # updated   更新日期（最新的优先）         updated, id
    # outdated  更新日期（最早的优先）         -updated, -id
    # newest    Creation(Newest First)      id
    # oldest    Creation(Oldest First)      -id
    # title     标题                      title, id
    def get_taskPHIDs_for_projectPHID(self, queryKey, projectPHID):
        self.set_method('maniphest.search')
        self.set_data({'queryKey[0]': queryKey})
        self.set_data({'projectPHIDs[0]': projectPHID})
        self.set_data({'order[0]': 'updated'})
        self.set_data({'order[1]': 'id'})
        print('get_taskPHIDs_for_projectPHID'.center(40, '='))
        return self.call_api()['result']

    def get_taskPHIDs_for_ownerPHID_authorPHID_projectPHID(self, ownerPHID, authorPHID, projectPHID):
        print('maniphest.query'.center(40, '='))
        self.set_method("maniphest.query")
        self.set_data({'ownerPHIDs[0]': ownerPHID})
        self.set_method({'authorPHIDs[0]': authorPHID})
        self.set_method({'projectPHIDs[0]': projectPHID})
        return list(self.call_api()['result'])


# 注意status以PH设置为准
# Open : 		open
# Resolved : 	resolved
# Wontfix : 	wontfix
# Invalid : 	invalid
# Spite : 		spite
def setTaskStatusForPHID(phid, status):
    print('maniphest.update'.center(40, '='))
    setMethod("maniphest.update")

    p = {'phid': phid}
    setData(p)
    s = {'status': status}
    setData(s)

    return callAPI()['result']['phid']


# 注意priority以PH设置为准
# Unbreak Now : 	100
# Needs Triage : 	90
# High : 			80
# Normal : 			50
# Low : 			25
# Wishlist : 		0
def setTaskPriorityForPHID(phid, priority):
    print('maniphest.update'.center(40, '='))
    setMethod("maniphest.update")

    p = {'phid': phid}
    setData(p)
    s = {'priority': priority}
    setData(s)

    return callAPI()['result']['phid']


def setCreateTask(title, description, ownerPHID, viewPolicy, editPolicy, projectPHIDs):
    print('maniphest.createtask'.center(40, '='))
    setMethod("maniphest.createtask")

    t = {'title': title}
    setData(t)
    # print(t)

    d = {'description': description}
    setData(d)
    # print(d)

    # ownerPHID is Assigned To
    if (ownerPHID):
        a = {'ownerPHID': ownerPHID}
        setData(a)
    # print(a)

    # viewPolicy is Visible To
    if (viewPolicy):
        v = {"viewPolicy": viewPolicy}
        setData(v)
    # print(v)

    # editPolicy is Editable By
    if (editPolicy):
        e = {"editPolicy": editPolicy}
        setData(e)
    # print(e)

    # projectPHIDs is Tags
    t = {"projectPHIDs[0]": projectPHIDs}
    setData(t)
    # print(t)

    return callAPI()['result']['phid']

# 查询个人信息
# print('call_api'.center(40,'='))
# ConduitAPI.setMethod("user.whoami")
# ConduitAPI.call_api()

# data = {'api.token':token}
# res = Conduit_API(method,data)
# print(res)
# print(type(res))

# method = "maniphest.createtask"
# data = {'api.token':token,'title':'这是一个测试'}
# res = Conduit_API(method,data)
# print(res)
# print(type(res))
