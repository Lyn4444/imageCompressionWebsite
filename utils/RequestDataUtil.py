from DataUtils import CreateData


class CreateRequestData(object):
    def __init__(self):
        self.request = CreateData()
        self.request.add_one("code")
        self.request.add_one("msg")
        self.request.add_one("data")

    def setCode(self, code):
        self.request.update("code", code)

    def setMsg(self, msg):
        self.request.update("msg", msg)

    def setData(self, data):
        self.request.update("data", data)

    def getRequestData(self):
        return self.request.get()