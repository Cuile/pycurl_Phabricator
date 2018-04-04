class user(object):
    def __init__(self, ph):
        self.base = ph

    def whoami(self):
        self.base.clear_data()
        self.base.set_method('user.whoami')
        return self.base.call_api()
