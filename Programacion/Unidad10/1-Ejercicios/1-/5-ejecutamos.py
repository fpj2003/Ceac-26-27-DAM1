from flask import Flask

aplicacion = Flask("__name__") #creamos nueva aplicación

@aplicacion.route("/")
def inicio():
	return "Si estas viendo esto te lo esta dando python"

if __name__ == "__main__":
  aplicacion.run()	
	
	
	

