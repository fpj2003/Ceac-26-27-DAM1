
# Primero importo la librería de conexión y la libreria web
import mysql.connector
from flask import Flask, render_template

# Me conecto a la base de datos, pero usando los datos que acabamos de crear
connection = mysql.connector.connect(
  host='localhost',
  user='curro',
  password='Ceac123$',
  database='curriculum'
)

# creo una aplicación web
aplicacion = Flask(__name__) 


@aplicacion.route("/")
def inicio():
  # Creo un cursor en modo diccionario para acceder por nombre de columna
  cursor = connection.cursor(dictionary=True)

  # 1. Recupero Datos Personales (solo necesitamos uno, usamos fetchone)
  cursor.execute("SELECT * FROM datos_personales ")
  datos_personales = cursor.fetchone()

  # 2. Recupero Datos de Contacto
  cursor.execute("SELECT * FROM datos_contacto ")
  contacto = cursor.fetchone()

  # 3. Recupero Redes Sociales
  cursor.execute("SELECT * FROM redes_sociales ")
  redes = cursor.fetchone()

  # 4. Recupero Experiencia Laboral (pueden ser varias, usamos fetchall)
  cursor.execute("SELECT * FROM experiencias_laborales")
  experiencias = cursor.fetchall()

  # 5. Recupero Formación
  cursor.execute("SELECT * FROM formacion")
  formaciones = cursor.fetchall()

  # 6. Recupero Idiomas
  cursor.execute("SELECT * FROM idiomas")
  idiomas = cursor.fetchall()

  # 7. Recupero Habilidades
  cursor.execute("SELECT * FROM conocimientos")
  conocimientos = cursor.fetchall()
  
  # Cierro el cursor (buena práctica después de hacer las consultas)
  cursor.close()

  # Envío todos los datos al HTML
  return render_template(
        "curriculum.html",
        datos_personales = datos_personales,
        contacto = contacto,
        redes = redes,
        experiencias = experiencias,
        formaciones = formaciones,
        idiomas = idiomas,
        conocimientos = conocimientos,

  )

if __name__ == "__main__":
  aplicacion.run(debug=True) 

connection.close()
