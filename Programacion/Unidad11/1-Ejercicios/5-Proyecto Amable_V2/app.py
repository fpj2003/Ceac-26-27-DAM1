from flask import Flask, render_template, request, jsonify
import requests
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Inicializar la base de datos automáticamente
def init_db():
    conn = sqlite3.connect("amable.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS webs
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  usuario TEXT,
                  fecha TEXT,
                  pregunta TEXT,
                  respuesta TEXT)''')
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/procesa", methods=['POST'])
def procesa():
    # Ahora recibimos JSON desde fetch (AJAX)
    pregunta_usuario = request.json.get('peticion', '')
    
    ruta = "http://localhost:11434/api/generate"
    modelo = "qwen2.5-coder:3b"
    
    sistema = """
        -Crea sitios web completos y funcionales
        -Dame SOLO EL CODIGO HTML
        -No me des markdown ni comillas triples
        -No me des explicaciones
        -No hagas comentarios
        -Solo se pueden pedir páginas web, no se puede pedir otra cosa
        -Atiende a la petición del usuario:
    """
    
    pregunta = sistema + pregunta_usuario
    flujo = False
    
    try:
        r = requests.post(ruta, json={
            "model": modelo,
            "prompt": pregunta,
            "stream": flujo
        })
        
        mirespuesta = str(r.json().get("response", ""))
        
        # Guardamos la respuesta en la base de datos
        conexion = sqlite3.connect("amable.db")
        cursor = conexion.cursor()
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        cursor.execute("""
            INSERT INTO webs
            VALUES (NULL, ?, ?, ?, ?)
        """, (
            "usuario_amable",
            fecha_actual,
            pregunta_usuario,
            mirespuesta
        ))
        
        conexion.commit()
        conexion.close()

        # Devolvemos un JSON para que Javascript actualice la interfaz sin recargar la página
        return jsonify({"status": "success", "codigo": mirespuesta})
        
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
