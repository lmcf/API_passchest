import xml.etree.ElementTree as ET
from controller.json_controller import JSONFile
from controller.logging_controller import RotatingLogger
from os.path import dirname

class ConfigController(object):
    def __init__(self):
        try:
            project_root = dirname(dirname(__file__))
            tree = ET.parse(project_root+"/config/config.xml")
            self.root = tree.getroot()

            self.appname = self.root.find("appname").text
            self.version = self.root.find("version").text
            self.mayus = int(self.root.find("password_defaults").find("mayus").text)
            self.lenght = int(self.root.find("password_defaults").find("lenght").text)
            self.digits = int(self.root.find("password_defaults").find("digits").text)
            self.symbols = int(self.root.find("password_defaults").find("symbols").text)

            self.data_path = self.root.find("data_path").text
            self.log_path = self.root.find("logs").find("path_logs").text
            self.max_files_x_log = self.root.find("logs").find("max_files_x_log").text
            self.max_size_x_log = self.root.find("logs").find("max_size_x_log").text
            self.debug_enable = self.root.find("logs").find("debug_enable").text

            self.log = RotatingLogger(self.log_path,self.max_size_x_log,self.max_files_x_log, self.debug_enable)
        except TypeError:
            print("Error de configuracion del fichero config.xml")

        try:
            self.json_file = JSONFile(self.data_path)
        except TypeError as e:
            print("ERROR al instanciar la clase JSONFILE")
           
            
    def passwordConfig(self):
        return {"MAYUS" : self.mayus, "LENGHT" : self.lenght, "DIGITS" : self.digits, "SYMBOLS" : self.symbols}

    def ping(self):
        return {"APPNAME" : self.appname,"VERSION" : self.version, "DEFAULT_SETTINGS":self.passwordConfig()}
