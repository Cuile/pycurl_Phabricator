#!/usr/bin/python
# -*- coding: utf-8 -*-
from io import BytesIO
import urllib.parse
import json

import pycurl
import certifi

url = token = method = ""
data = {}


def setUrl(u):
    global url
    url = u


# print("setUrl : %s" % (url))

def setToken(t):
    global token
    token = t
    print("setToken : %s" % (token))
    setData({'api.token': token})


def setMethod(m):
    global url, method
    method = url + m


# print("setMethod : %s" % (method))

def setData(d):
    global data
    data.update(d)


# print("setData : %r" % (data))

def clearData():
    global data
    data = {}
    setData({'api.token': token})


def callAPI():
    global method, data

    buffer = BytesIO()

    c = pycurl.Curl()

    c.setopt(c.CAINFO, certifi.where())
    # c.setopt(c.VERBOSE, True)
    c.setopt(c.POST, True)
    c.setopt(c.POSTFIELDS, urllib.parse.urlencode(data))
    # print(urllib.parse.urlencode(data))

    c.setopt(c.URL, method)
    c.setopt(c.WRITEFUNCTION, buffer.write)

    c.perform()
    c.close()

    # print("buffer : %s" % (buffer.getvalue()))
    b = buffer.getvalue().decode("utf-8")
    # print("callAPI : %s" % (b))
    clearData()

    return json.loads(b)


def getUserPHIDForUserName(userName):
    # print('user.query'.center(40,'='))
    setMethod("user.query")
    # print(userName)
    u = {'usernames[0]': userName}
    setData(u)
    r = callAPI()['result'][0]['phid']
    print("User Name is: %s, PHID is: %s" % (userName, r))
    return


def getProjectPHIDForName(names):
    # print('project.query'.center(40,'='))
    setMethod("project.query")
    # print(names)
    n = {'names[0]': names}
    setData(n)
    r = list(callAPI()['result']['data'])[0]
    print("Project Name is: %s, PHID is: %s" % (names, r))
    return r


def getTaskPHIDsForOwnerAuthorProject(ownerPHID, authorPHID, projectPHID):
    print('maniphest.query'.center(40, '='))
    setMethod("maniphest.query")
    o = {'ownerPHIDs[0]': ownerPHID}
    setData(o)
    a = {'authorPHIDs[0]': authorPHID}
    setData(a)
    p = {'projectPHIDs[0]': projectPHID}
    setData(p)
    # l = {'limit':1}
    # setData(l)
    return list(callAPI()['result'])


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
# print('callAPI'.center(40,'='))
# ConduitAPI.setMethod("user.whoami")
# ConduitAPI.callAPI()

# data = {'api.token':token}
# res = Conduit_API(method,data)
# print(res)
# print(type(res))

# method = "maniphest.createtask"
# data = {'api.token':token,'title':'这是一个测试'}
# res = Conduit_API(method,data)
# print(res)
# print(type(res))
