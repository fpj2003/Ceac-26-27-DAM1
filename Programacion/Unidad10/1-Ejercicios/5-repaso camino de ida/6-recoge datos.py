from flask import Flask,render_template

aplicacion = Flask("__name__") 

@aplicacion.route("/")
def inicio():
  return render_template("formulario.html")

@aplicacion.route("/recogedatos",methods=['POST'])
def recogedatos():
  cadena="" 
  cadena += "Nombre del médico "+request.form['nombre']+"<br"  
  cadena += "Especialidad del médico "+request.form['especialidad']+"<br"  
  cadena += "Numero de colegiado del médico "+request.form['numero_de_colegiado']+"<br"  
  return cadena



if __name__ == "__main__":
  aplicacion.run()
  
  
  
  

