from flask import Flask, render_template

aplicacion = Flask("__name__") 

@aplicacion.route("/")
def inicio():
  return render_template(
    	"index3.html",
      nombre = "Fernando",
      apellidos = "Puig Jorda",
      email = "fpj2003@gmail.com"
  )
  
if __name__ == "__main__":
  aplicacion.run()
