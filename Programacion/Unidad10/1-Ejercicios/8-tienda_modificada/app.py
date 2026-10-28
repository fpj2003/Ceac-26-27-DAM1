from flask import Flask, render_template, request, session, redirect, url_for
import json
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'clave_secreta_super_segura' # Necesario para usar sesiones

def get_db_connection():
    conn = sqlite3.connect("tienda.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def inicio():
    return render_template("tienda.html")

@app.route("/datos")
def datos():
    conn = get_db_connection()
    productos = conn.execute("SELECT * FROM productos").fetchall()
    conn.close()
    return json.dumps([dict(p) for p in productos])

@app.route("/insertapedido", methods=['POST'])
def insertapedido():
    fecha = datetime.now()
    data = request.get_json()
    cliente = data.get('cliente', {})
    pedido = data.get('pedido', [])
    
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO pedidos (numerodepedido, fecha, nombre_cliente, apellidos_cliente, correo_cliente, carga) VALUES (?, ?, ?, ?, ?, ?)",
        (str(fecha.timestamp()), str(fecha), cliente.get('nombre', ''), cliente.get('apellidos', ''), cliente.get('correo', ''), json.dumps(pedido, ensure_ascii=False))
    )
    conn.commit()
    conn.close()
    return "ok"

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form.get('password') == 'admin':
            session['admin_logged_in'] = True
            return redirect(url_for('admin'))
        else:
            return render_template('login.html', error="Contraseña incorrecta")
    return render_template('login.html')

@app.route("/logout")
def logout():
    session.pop('admin_logged_in', None)
    return redirect(url_for('inicio'))

@app.route("/admin")
def admin():
    if not session.get('admin_logged_in'):
        return redirect(url_for('login'))
        
    conn = get_db_connection()
    pedidos = conn.execute("SELECT * FROM pedidos ORDER BY id DESC").fetchall()
    conn.close()
    
    pedidos_procesados = []
    for p in pedidos:
        try:
            carga = json.loads(p['carga'])
        except:
            carga = []
        pedidos_procesados.append({
            'id': p['id'],
            'fecha': p['fecha'],
            'nombre': p['nombre_cliente'],
            'apellidos': p['apellidos_cliente'],
            'correo': p['correo_cliente'],
            'carga': carga
        })
        
    return render_template("admin.html", pedidos=pedidos_procesados)

if __name__ == "__main__":
    app.run(debug=True)
