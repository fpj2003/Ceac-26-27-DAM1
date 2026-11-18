from flask import Flask, render_template, request

import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='examendamceac2627',
    password='CEACExamenDAM123$',
    database='examendamceac2627'
)

cursor = connection.cursor(dictionary=True)
# Creo una aplicación web
aplicacion = Flask(__name__) 

@aplicacion.route("/")
def inicio():
    
    cursor.execute("SELECT * FROM medicos")
    medicos = cursor.fetchall()
    return render_template("frente.html", medicos=medicos)
    
@aplicacion.route("/formulario")
def formulario():
    return render_template("formulario.html")

@aplicacion.route("/inserta", methods=['POST'])
def inserta():
    cursor.execute("""   
        INSERT INTO medicos VALUES(
            NULL,
            '""" + request.form['nombre'] + """',
            '""" + request.form['apellidos'] + """',
            '""" + request.form['email'] + """',
            '""" + request.form['especialidad'] + """',
            '""" + request.form['numero_de_colegiado'] + """',
            '""" + request.form['activo'] + """'
        );
    """)
    connection.commit()
    return render_template("inserta.html")
   
    
if __name__ == "__main__":
    aplicacion.run()      
