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
    
if __name__ == "__main__":
    aplicacion.run()    
