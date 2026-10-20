from flask import Flask, render_template

aplicacion = Flask("__name__") 

@aplicacion.route("/")
def inicio():
  return render_template(
    	"index4.html",
    	frutas=["manzanas","peras","platano"]
  )
  
if __name__ == "__main__":
  aplicacion.run()
