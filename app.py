from contextlib import nullcontext
from flask import Flask, request
from controller.master_controller import MasterController

app = Flask(__name__)

@app.route("/ping")
def ping():
   return master.config.ping()


# Genera password en base a parametros
@app.route("/generatepassword")
def generatepassword():
   lenght = request.args.get("lenght", default=int(master.config.lenght), type=int)
   mayus = request.args.get("mayus", default=master.config.mayus, type=int)
   digits = request.args.get("digits", default=master.config.digits, type=int)
   symbols = request.args.get("symbols", default=master.config.symbols, type=int)
   print(symbols)
   return master.generatepassword(lenght, mayus, digits, symbols)

# Guarda la contraseña generada, con los datos de la aplicación donde se usara
# siteweb, username and password
@app.route("/savepassword")
def savepassword():
   aData = generatepassword()
   aData['USERNAME'] = request.args.get("username", default="", type=str)
   aData['APLICATION'] = request.args.get("app", default="", type=str)
   print("aDATA a guardar #1-> ",aData)
   return master.saveinJson(aData)

# Devuelve todas las contraseñas almacenadas
@app.route("/getpasswords")
def getpasswords():
   id = request.args.get("id", default = nullcontext, type=int)
   return  master.getPasswordByID(id) if id != nullcontext else master.getAllPasswords() 

@app.route("/help")
def help():
   return master.getHelp()

if __name__ == "__main__":
    master = MasterController()
    app.run()