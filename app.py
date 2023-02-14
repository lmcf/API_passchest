from contextlib import nullcontext
from flask import Flask, request
from controller.master_controller import MasterController
import base64


app = Flask(__name__)
@app.route("/ping")
def ping():
   master.log.debug(ping.__name__)
   return master.config.ping()

@app.route("/generatekey")
def generatekey():
   master.log.debug(generatekey.__name__)
   return master.security.generated_key()

# Genera password en base a parametros
@app.route("/generatepassword")
def generatepassword():
   lenght = request.args.get("lenght", default=int(master.config.lenght), type=int)
   mayus = request.args.get("mayus", default=master.config.mayus, type=int)
   digits = request.args.get("digits", default=master.config.digits, type=int)
   symbols = request.args.get("symbols", default=master.config.symbols, type=int)
   return master.generatepassword(lenght, mayus, digits, symbols)

# Guarda la contraseña generada, con los datos de la aplicación donde se usara
# siteweb, username and password
@app.route("/savepassword")
def savepassword():
   master_key = request.args.get("master_key", type=str)
   master.security.setup(master_key)
   aData = {}
   aData["USERNAME"] = request.args.get("username", default="", type=str)
   aData["APLICATION"] = request.args.get("app", default="", type=str)
   passw =  master.security.encrypt(request.args.get("password", default=generatepassword(), type=str))
   print(passw)
   aData["PASSWORD"] =  passw.decode(master.security.encoding)
   return master.saveinJson(aData)

# Devuelve todas las contraseñas almacenadas
@app.route("/getpasswords")
def getpasswords():
   master_key = request.args.get("master_key", type=str)
   master.security.setup(master_key)
   id = request.args.get("id", default = nullcontext, type=int)
   itemData =  master.getPasswordByID(id) if id != nullcontext else master.getAllPasswords()
   if id != nullcontext:
      itemData['PASSWORD'] = master.security.decrypt(str(itemData['PASSWORD']).encode())
   else:
      for key, value in itemData.items():
         value['PASSWORD'] =  master.security.decrypt(str(value['PASSWORD']).encode())

   return itemData

@app.route("/")
def help():
   return master.getHelp()

if __name__ == "__main__":
    master = MasterController()
    app.run()