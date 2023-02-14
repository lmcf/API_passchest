import random
import string
from controller.config_controller import RotatingLogger


class PasswordController:
    def __init__(self,default_pass):
        self.mayus = int(default_pass['MAYUS'])
        self.lenght = int(default_pass['LENGHT'])
        self.digits = int(default_pass['DIGITS'])
        self.symbols = int(default_pass['SYMBOLS'])
        self.passw = ""
       

    def getDefaults(self):
        return {"MAYUS" : self.mayus, "LENGHT" : self.lenght, "DIGITS" : self.digits, "SYMBOLS" : self.symbols}
    
    def withMayus(self):
        return True if self.mayus == 1 else False
    
    def withDigits(self):
        return True if self.digits == 1 else False

    def withSymbols(self):
        return True if self.symbols == 1 else False    

    def get_random_password(self):
        data = [string.ascii_lowercase]
        
        if self.withMayus():
            data.append(string.ascii_uppercase)
        
        if self.withDigits():
            data.append(string.digits)
            
        if self.withSymbols():
            data.append(string.punctuation.replace(",","").replace(".","").replace("<","").replace(">",""))
            
        passw = ""

        for num in range(0, int(self.lenght), 1):
            type = random.choice(data)
            caracter = random.choice(type)
            passw += caracter

        self.passw = passw
        return self.passw

