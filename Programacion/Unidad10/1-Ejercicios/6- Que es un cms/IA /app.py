from flask import Flask, render_template, request, session, redirect, url_for
import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='blogceacdam2627',
    password='Ceac123$',
    database='blogceacdam2627'
)
cursor = connection.cursor(dictionary=True)

app = Flask(__name__) 
app.secret_key = 'super_secreta_y_segura_123' 

@app.route("/")
def inicio():
    cursor.execute("SELECT * FROM articulos")
    articulos = cursor.fetchall()
    return render_template("frente.html", articulos=articulos)

@app.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['usuario'] == 'admin' and request.form['password'] == 'admin123$':
            session['logeado'] = True
            return redirect(url_for('tabla')) # Redirige a la tabla automáticamente
        else:
            error = "Usuario o contraseña incorrectos"
    return render_template("login.html", error=error)

@app.route("/logout")
def logout():
    session.pop('logeado', None)
    return redirect(url_for('inicio'))

@app.route("/tabla")
def tabla():
    if not session.get('logeado'):
        return redirect(url_for('login'))
        
    cursor.execute("SELECT * FROM articulos")
    todoslosarticulos = cursor.fetchall()
    return render_template("tabla.html", tepasolosarticulos=todoslosarticulos)

@app.route("/formulario")
def formulario():
    if not session.get('logeado'):
        return redirect(url_for('login'))
    return render_template("formulario.html")

@app.route("/inserta", methods=['POST'])
def inserta():
    if not session.get('logeado'):
        return redirect(url_for('login'))
        
    cursor.execute("""   
        INSERT INTO articulos VALUES(
            NULL,
            '""" + request.form['titulo'] + """',
            '""" + request.form['fecha'] + """',
            '""" + request.form['contenido'] + """'
        );
    """)
    connection.commit()
    return render_template("inserta.html")

if __name__ == "__main__":
    app.run(debug=True)
