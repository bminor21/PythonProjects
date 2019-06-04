class DbBase(object):
    def __init__(self):
        pass

    def executeStatement(self, statement):
        raise NotImplementedError()
