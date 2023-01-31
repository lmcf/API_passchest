import json

class JSONFile:
    def __init__(self, path):
        self.path = (path+'data.json')
        self.help_path = ('help.json')
        print("PATH SETEADO -> ",self.path)

    def write(self, new_data):
        new_file = False
        print("aDATA a guardar #2-> ",new_data)
        try:
            old_data = self.read()
        except FileNotFoundError:
            new_file = True
            old_data = {}

        new_data = {100:new_data} if new_file == True else {100 + len(old_data) : new_data}
        old_data.update(new_data)
        with open(self.path, "w") as file:
            json.dump(old_data, file)

        return new_data

    def read(self, help = False):
        path = self.path if help == False else self.help_path
        with open(path, "r") as file:
            return json.load(file)

    def searchAll(self):
         return dict(sorted(self.read().items()))