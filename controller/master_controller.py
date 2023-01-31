from contextlib import nullcontext
from controller.config_controller import ConfigController
from controller.password_controller import PasswordController

class MasterController(object):
    def __init__(self):
        self.config =  ConfigController()
        self.default_pass_config = self.config.passwordConfig()
        self.cPassword = PasswordController(self.default_pass_config)
        self.json_file = self.config.json_file

    def generatepassword(self, lenght = nullcontext, mayus = nullcontext, digits = nullcontext, symbols = nullcontext):
        self.cPassword.lenght = lenght if lenght != nullcontext else int(self.cPassword.lenght)
        self.cPassword.mayus = mayus if mayus != nullcontext else int(self.cPassword.mayus)
        self.cPassword.digits = digits if digits != nullcontext else int(self.cPassword.digits)
        self.cPassword.symbols = symbols if symbols != nullcontext else int(self.cPassword.symbols)
        return self.cPassword.get_random_password()


    def saveinJson(self, objectData):
        return self.json_file.write(objectData)

    def getAllPasswords(self):
        return self.json_file.searchAll()
    
    def getPasswordByID(self, id):
        allData = self.json_file.searchAll()
        return allData.get(str(id)) if allData.get(str(id)) else False

    def getHelp(self):
        return self.json_file.read(True)
