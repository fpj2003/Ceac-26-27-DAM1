from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__) 

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='examendamceac2627',
        password='CEACExamenDAM123$',
        database='examendamceac2627'
    )

@app.route("/")
def inicio():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM medicos")
        medicos = cursor.fetchall()
        cursor.close()
        connection.close()
    except Exception as e:
        print(f"Error de conexión: {e}")
        # Datos de prueba por si la base de datos falla, para poder ver el diseño
        medicos = [] 
        
    return render_template("frente.html", medicos=medicos)
    
@app.route("/formulario")
def formulario():
    return render_template("formulario.html")

@app.route("/inserta", methods=['POST'])
def inserta():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        # MEJORA: Consultas parametrizadas para evitar Inyección SQL
        query = '''INSERT INTO medicos (nombre, apellidos, email, especialidad, numero_de_colegiado, activo) 
                   VALUES (%s, %s, %s, %s, %s, %s)'''
        values = (
            request.form['nombre'],
            request.form['apellidos'],
            request.form['email'],
            request.form['especialidad'],
            request.form['numero_de_colegiado'],
            request.form['activo']
        )
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        connection.close()
    except Exception as e:
        print(f"Error al insertar: {e}")
        
    # MEJORA: Redirigir a la lista principal después de insertar
    return redirect(url_for('inicio'))

if __name__ == "__main__":
    app.run(debug=True)
