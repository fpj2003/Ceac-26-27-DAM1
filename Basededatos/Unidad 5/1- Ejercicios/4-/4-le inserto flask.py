from flask import Flask, render_template, request
import sqlite3

# Me conecto a la base de datos SQLite
conexion = sqlite3.connect("blog.db", check_same_thread=False)
conexion.row_factory = sqlite3.Row

# Creo el cursor de SQLite
cursor = conexion.cursor()

# Creo una aplicación web
aplicacion = Flask(__name__) 

# Defino la ruta de inicio
@aplicacion.route("/")
def inicio():
    # Dame todos los articulos de la base de datos
    cursor.execute("SELECT * FROM articulos")
    # Los meto en una variable
    articulos = cursor.fetchall()
    # Llamo a la plantilla Y LE PASO LOS ARTICULOS
    return render_template("frente.html", articulos=articulos)

@aplicacion.route("/tabla")
def tabla():
    # Dame todos los articulos de la base de datos
    cursor.execute("SELECT * FROM articulos")
    # Los meto en una variable
    todoslosarticulos = cursor.fetchall()
    # Llamo a la plantilla Y LE PASO LOS ARTICULOS
    return render_template("tabla.html", tepasolosarticulos=todoslosarticulos)

@aplicacion.route("/formulario")
def formulario():
    return render_template("formulario.html")

@aplicacion.route("/inserta", methods=['POST'])
def inserta():
    cursor.execute("""   
        INSERT INTO articulos VALUES(
            NULL,
            '""" + request.form['titu
            
            lo'] + """',
            '""" + request.form['fecha'] + """',
            '""" + request.form['contenido'] + """'
        );
    """)
    conexion.commit()
    return render_template("inserta.html")

@aplicacion.route("/recibedatos", methods=['POST'])
def recibedatos():
    cursor.execute("""   
        INSERT INTO contacto VALUES(
            NULL,
            '""" + request.form['nombre'] + """',
            '""" + request.form['correo'] + """',
            '""" + request.form['mensaje'] + """'
        );
    """)
    conexion.commit()
    return render_template("confirmacion.html")

if __name__ == "__main__":
    aplicacion.run(debug=True)
    
conexion.close()
