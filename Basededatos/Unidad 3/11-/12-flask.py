# Primero importo las librerías
import mysql.connector # Primero importo MySQL
from flask import Flask # Y también importo Flask

# Me conecto con las credenciales correctas
connection = mysql.connector.connect(
    host='localhost',
    user='formula',
    password='Formula123$',
    database='formula1'
)

# Creo un cursor
cursor = connection.cursor()

# Ahora creo una aplicación base
aplicacion = Flask("__name__") 

# Defino un punto donde flask va a escuchar en la web
@aplicacion.route("/")
def inicio():
    # Creo una cadena vacia
    cadena = """
        <!doctype html>
        <html>
            <head>
                <style>
                    article{border:1px solid grey;padding:10px;margin:10px;}
                </style>
            </head>
            <body>
            <h1>Parrilla temporada 2026</h1>
            <form action="/mostrar_ferrari">
                <button type="submit">Ver pilotos de Ferrari</button>
            </form>
                        <form action="/mostrar_aston">
                <button type="submit">Ver pilotos de Aston Martin</button>
            </form>
            <form action="/mostrar_mercedes">
                <button type="submit">Ver pilotos de Mercedes</button>
            </form>
            
     """
    # Ejecuto una petición a la base de datos
    cursor.execute("SELECT * FROM piloto")	
    # Recupero el resultado de la petición
    filas = cursor.fetchall()	
    # Recorro el resultado
    for fila in filas:
        cadena += """
            <article>
                <h3>"""+fila[1]+" "+fila[2]+"""</h3>
                <p>"""+fila[3]+"""</p>
                <p>"""+fila[4]+"""</p>
                <p>"""+str(fila[3])+"""</p>
            </article>
        """
    # Lo devuelvo a HTML
    return cadena
  
@aplicacion.route("/mostrar_ferrari")
def mostrar_ferrari():
    # Creo una cadena vacia
    cadena = """
        <!doctype html>
        <html>
            <head>
                <style>
                    article{border:1px solid grey;padding:10px;margin:10px;}
                </style>
            </head>
            <body>
            <h1>Parrilla temporada 2026</h1>
            <form action="/mostrar_ferrari">
                <button type="submit">Ver pilotos de Ferrari</button>
            </form>
                        <form action="/mostrar_aston">
                <button type="submit">Ver pilotos de Aston Martin</button>
            </form>
            <form action="/mostrar_mercedes">
                <button type="submit">Ver pilotos de Mercedes</button>
            </form>
            
            <form action="/">
                <button type="submit">Mostrar todo</button>
            </form>
    """
    # Ejecuto una petición a la base de datos
    cursor.execute("SELECT * FROM piloto WHERE escuderia= 'Ferrari' ")	
    # Recupero el resultado de la petición
    filas = cursor.fetchall()	
    # Recorro el resultado
    for fila in filas:
        cadena += """
            <article>
                <h3>"""+fila[1]+" "+fila[2]+"""</h3>
                <p>"""+fila[3]+"""</p>
                <p>"""+fila[4]+"""</p>
                <p>"""+str(fila[3])+"""</p>
            </article>
        """
    # Lo devuelvo a HTML
    return cadena  

@aplicacion.route("/mostrar_aston")
def mostrar_aston():
    # Creo una cadena vacia
    cadena = """
        <!doctype html>
        <html>
            <head>
                <style>
                    article{border:1px solid grey;padding:10px;margin:10px;}
                </style>
            </head>
            <body>
            <h1>Parrilla temporada 2026</h1>
            <form action="/mostrar_ferrari">
                <button type="submit">Ver pilotos de Ferrari</button>
            </form>
            <form action="/mostrar_aston">
                <button type="submit">Ver pilotos de Aston Martin</button>
            </form>
            <form action="/mostrar_mercedes">
                <button type="submit">Ver pilotos de Mercedes</button>
            </form>
            
            <form action="/">
                <button type="submit">Mostrar todo</button>
            </form>
    """
    # Ejecuto una petición a la base de datos
    cursor.execute("SELECT * FROM piloto WHERE escuderia= 'Aston Martin' ")	
    # Recupero el resultado de la petición
    filas = cursor.fetchall()	
    # Recorro el resultado
    for fila in filas:
        cadena += """
            <article>
                <h3>"""+fila[1]+" "+fila[2]+"""</h3>
                <p>"""+fila[3]+"""</p>
                <p>"""+fila[4]+"""</p>
                <p>"""+str(fila[3])+"""</p>
            </article>
        """
    # Lo devuelvo a HTML
    return cadena    
  
@aplicacion.route("/mostrar_mercedes")
def mostrar_mercedes():
    # Creo una cadena vacia
    cadena = """
        <!doctype html>
        <html>
            <head>
                <style>
                    article{border:1px solid grey;padding:10px;margin:10px;}
                </style>
            </head>
            <body>
            <h1>Parrilla temporada 2026</h1>
            <form action="/mostrar_ferrari">
                <button type="submit">Ver pilotos de Ferrari</button>
            </form>
            <form action="/mostrar_aston">
                <button type="submit">Ver pilotos de Aston Martin</button>
            </form>
            <form action="/mostrar_mercedes">
                <button type="submit">Ver pilotos de Mercedes</button>
            </form>
            
            <form action="/">
                <button type="submit">Mostrar todo</button>
            </form>
    """
    # Ejecuto una petición a la base de datos
    cursor.execute("SELECT * FROM piloto WHERE escuderia= 'Mercedes' ")	
    # Recupero el resultado de la petición
    filas = cursor.fetchall()	
    # Recorro el resultado
    for fila in filas:
        cadena += """
            <article>
                <h3>"""+fila[1]+" "+fila[2]+"""</h3>
                <p>"""+fila[3]+"""</p>
                <p>"""+fila[4]+"""</p>
                <p>"""+str(fila[3])+"""</p>
            </article>
        """
    # Lo devuelvo a HTML
    return cadena    
   
# Ejecuto la aplicación
if __name__ == "__main__":
    aplicacion.run()

# Todo lo que se abre se debe cerrar
cursor.close()
connection.close()
