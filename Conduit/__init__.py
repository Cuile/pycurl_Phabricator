# !/usr/bin/python
# -*- coding: utf-8 -*-

from io import BytesIO
import urllib.parse
import json

import pycurl
import certifi
import sequence2hash

from .user import *
from .maniphest import *
from .project import *


# __all__ = ['API']


class API(object):
    url = token = method_name = ''
    __method_data = {}

    def __set_data(self, data):
        self.__method_data.clear()
        self.__method_data.update({'api.token': self.token})
        for x in sequence2hash.flatten(data):
            if len(x['key']) == 1:
                self.__method_data.update({x['key'][0]: x['value']})
            else:
                self.__method_data.update({x['key'][0] + '[' + ']['.join(x['key'][1:]) + ']': x['value']})

    def call_method(self, method_name, method_data, result_type='dict'):
        self.__set_data(method_data)

        buffer = BytesIO()

        c = pycurl.Curl()
        c.setopt(c.CAINFO, certifi.where())
        # c.setopt(c.VERBOSE, True)
        c.setopt(c.POST, True)
        c.setopt(c.POSTFIELDS, urllib.parse.urlencode(self.__method_data))
        # print(urllib.parse.urlencode(self.__method_data, safe='/[]', quote_via=urllib.parse.quote))
        c.setopt(c.URL, self.url + method_name)
        c.setopt(c.WRITEFUNCTION, buffer.write)
        c.perform()
        c.close()

        b = buffer.getvalue().decode("utf-8")

        if result_type == 'dict':
            return json.loads(b)
        else:
            return json.dumps(json.loads(b), ensure_ascii=False)
