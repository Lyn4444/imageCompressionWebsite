class CreateData(object):
    def __init__(self):
        self.data = {}

    def add_one(self, name):
        if name not in self.data.keys():
            self.data.update({name: None})

    def add(self, name, data):
        if name in self.data.keys():
            return False
        else:
            self.data[name] = data
            return True

    def delete(self, name):
        del self.data[name]

    def update(self, name, data):
        self.data.update({name: data})

    def isHave(self, name):
        return name in self.data.keys()

    def get(self):
        return self.data
