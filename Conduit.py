#!/usr/bin/python
# -*- coding: utf-8 -*-
from io import BytesIO
import urllib.parse
import json

import pycurl
import certifi


class Conduit(object):
    """使用pycurl对Phabricator进行访问"""
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
