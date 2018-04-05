class user(object):
    def __init__(self, ph):
        self._base = ph

    def whoami(self):
        self._base.set_method('user.whoami')
        self._base.clear_data()
        return self._base.call_method()
