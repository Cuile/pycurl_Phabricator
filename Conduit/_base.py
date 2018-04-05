from io import BytesIO
import urllib.parse
import json

import pycurl
import certifi
from jsonpath import jsonpath


class Conduit(object):
    conduit_api_url = None
    conduit_api_token = None
    conduit_method_name = None
    conduit_method_data = {}
    conduit_method_api = None

    def set_url(self, u):
        self.conduit_api_url = u

    def set_token(self, t):
        self.conduit_api_token = t
        self.set_data({'api.token': self.conduit_api_token})

    def set_data(self, d):
        self.conduit_method_data.update(d)
        # print(self.method_data)

    def reset_data(self):
        self.conduit_method_data.clear()
        self.set_data({'api.token': self.conduit_api_token})

    def clear_data(self):
        self.conduit_method_data.clear()

    def set_method(self, m):
        self.conduit_method_api = self.conduit_api_url + m

    def call_method(self, api):
        self.set_method(api.method)
        self.set_data(api.parameters)

        buffer = BytesIO()

        c = pycurl.Curl()

        c.setopt(c.CAINFO, certifi.where())
        # c.setopt(c.VERBOSE, True)
        c.setopt(c.POST, True)
        c.setopt(c.POSTFIELDS, urllib.parse.urlencode(self.conduit_method_data))
        print(urllib.parse.urlencode(self.conduit_method_data))

        c.setopt(c.URL, self.conduit_method_api)
        c.setopt(c.WRITEFUNCTION, buffer.write)

        c.perform()
        c.close()

        # print("buffer : %s" % (buffer.getvalue()))
        b = buffer.getvalue().decode("utf-8")
        # print("call_api : %s" % (b))
        self.reset_data()

        return json.loads(b)
