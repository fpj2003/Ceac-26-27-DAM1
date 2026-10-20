# Importo Flask para la web y connector para MySQL
from flask import Flask, render_template, request
import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='caminodeida',
    password='Ceac123$',
    database='caminodeida'
)

aplicacion = Flask(__name__) 

@aplicacion.route("/")
def inicio():
    return render_template("index.html")

@aplicacion.route("/pelicula")
def peliculas():
	return render_template("pelicula.html")
@aplicacion.route("/serie")
def series():
	return render_template("serie.html")	
@aplicacion.route("/procesa_pelicula", methods=["POST"])
def procesa_pelicula():
    ######################### MYSQL
    # Creo un cursor para poder pedir cosas
    cursor = connection.cursor()

    # Ejecuto una petición sobre el cursor
    cursor.execute("""
        INSERT INTO peliculas (nombre, director, estreno)
        VALUES (%s, %s, %s);
    """, (
        request.form["nombre"],
        request.form["director"],
        request.form["estreno"]
    ))

    connection.commit()
    
    # Ahora atrapo los parametros
    cadena = ""
    cadena += request.form["nombre"]
    cadena += request.form["director"]
    cadena += request.form["estreno"]
    return "ok yo te voy a procesar el formulario: " + cadena 
  
@aplicacion.route("/procesa_serie", methods=["POST"])
def procesa_serie():
    ######################### MYSQL
    # Creo un cursor para poder pedir cosas
    cursor = connection.cursor()

    # Ejecuto una petición sobre el cursor
    cursor.execute("""
        INSERT INTO series (nombre, director, estreno)
        VALUES (%s, %s, %s);
    """, (
        request.form["nombre"],
        request.form["director"],
        request.form["estreno"]
    ))

    connection.commit()
    
    # Ahora atrapo los parametros
    cadena = ""
    cadena += request.form["nombre"]
    cadena += request.form["director"]
    cadena += request.form["estreno"]
    return "ok yo te voy a procesar el formulario: " + cadena 
    
if __name__ == "__main__":
    aplicacion.run()
