import xml.etree.ElementTree as ET
from controller.json_controller import JSONFile

class ConfigController(object):
    def __init__(self):
        try:
            tree = ET.parse("config/config.xml")
            self.root = tree.getroot()
        except TypeError:
            print("Error de configuracion del fichero config.xml")

        self.appname = self.root.find("appname").text
        self.version = self.root.find("version").text
        self.mayus = int(self.root.find("password_defaults").find("mayus").text)
        self.lenght = int(self.root.find("password_defaults").find("lenght").text)
        self.digits = int(self.root.find("password_defaults").find("digits").text)
        self.symbols = int(self.root.find("password_defaults").find("symbols").text)

        self.data_path = self.root.find("data_path").text

        try:
            self.json_file = JSONFile(self.data_path)
        except TypeError:
            print("ERROR al instanciar la clase JSONFILE")
           
            
    def passwordConfig(self):
        return {"MAYUS" : self.mayus, "LENGHT" : self.lenght, "DIGITS" : self.digits, "SYMBOLS" : self.symbols}

    def ping(self):
        return {"APPNAME" : self.appname,"VERSION" : self.version}
