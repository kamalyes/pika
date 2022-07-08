from hutools.mock import Mock

class PikaMock(object):
    def __init__(self):
        self.mock = Mock()

    def request(self, flow):
        pass
