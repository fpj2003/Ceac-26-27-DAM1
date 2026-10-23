from flask import Flask,render_template,request
import mysql.connector

connection = mysql.connector.connect(
        host='localhost',
        user='medicos',
        password='Ceac123$',
        database='medicos'
    )


aplicacion = Flask("__name__") 

@aplicacion.route("/")
def inicio():
  return render_template("formulario.html")

@aplicacion.route("/recogedatos",methods=['POST'])
def recogedatos():
  cursor = connection.cursor()
  cursor.execute("""
        INSERT INTO medicos (nombre, especialidad, numero_de_colegiado)
        VALUES (%s, %s, %s);
    """, (
        request.form["nombre"],
        request.form["especialidad"],
        request.form["numero_de_colegiado"]
    ))
  connection.commit()
  return render_template("confirmacion.html")
  cursor.close()

@aplicacion.route("/mostrar")
def mostrar():
  cursor = connection.cursor(dictionary=True)
  cursor.execute("SELECT * FROM medicos") # Saco los proyectos de la base de datos
  medicos = cursor.fetchall()		# Los meto en una variable
  return render_template("mostrar.html",medicos=medicos) # Y se los paso a la plantilla

if __name__ == "__main__":
  aplicacion.run()

cursor.close()
conexion.close()

