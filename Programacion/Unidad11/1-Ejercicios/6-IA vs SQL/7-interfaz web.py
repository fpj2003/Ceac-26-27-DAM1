
from flask import Flask, render_template, request, jsonify
import requests
import sqlite3
import re

app = Flask(__name__)

RUTA_OLLAMA = "http://localhost:11434/api/generate"
MODELO = "duckdb-nsql"
BASE_DATOS = "empresa.db"


def obtener_estructura():
    """Obtiene automáticamente las tablas y columnas de SQLite."""
    conexion = sqlite3.connect(BASE_DATOS)
    try:
        cursor = conexion.cursor()

        cursor.execute("""
            SELECT name FROM sqlite_master
            WHERE type = 'table'
            AND name NOT LIKE 'sqlite_%'
        """)

        tablas = cursor.fetchall()
        estructura = []

        for (tabla,) in tablas:
            nombre_seguro = tabla.replace('"', '""')
            cursor.execute(f'PRAGMA table_info("{nombre_seguro}")')
            columnas = cursor.fetchall()

            campos = ", ".join(
                f'"{columna[1]}" {columna[2]}'
                for columna in columnas
            )

            estructura.append(f'TABLA "{tabla}": {campos}')

        return "\n".join(estructura)
    finally:
        conexion.close()


def generar_sql(pregunta):
    estructura = obtener_estructura()

    prompt = f"""
Eres un experto en SQLite.

Convierte la petición del usuario en una consulta SQL.

REGLAS:
- Devuelve exclusivamente SQL.
- No incluyas markdown ni explicaciones.
- Utiliza únicamente tablas y columnas existentes.
- Genera una sola sentencia SELECT.
- No utilices INSERT, UPDATE, DELETE, DROP ni ALTER.
- Utiliza sintaxis compatible con SQLite.

ESTRUCTURA:
{estructura}

PETICIÓN:
{pregunta}

SQL:
"""

    respuesta = requests.post(
        RUTA_OLLAMA,
        json={
            "model": MODELO,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0
            }
        },
        timeout=120
    )

    respuesta.raise_for_status()

    sql = respuesta.json()["response"].strip()

    sql = re.sub(r"```(?:sql)?", "", sql, flags=re.I)
    sql = sql.replace("```", "").strip()

    return sql


def ejecutar_sql(sql):
    # Solo permitimos una sentencia de lectura.
    # SQLite read-only evita modificaciones aunque el modelo falle.
    conexion = sqlite3.connect(
        f"file:{BASE_DATOS}?mode=ro",
        uri=True
    )

    try:
        conexion.execute("PRAGMA query_only = ON")
        cursor = conexion.cursor()

        cursor.execute(sql)

        if cursor.description is None:
            raise ValueError("La consulta no devuelve resultados.")

        columnas = [
            descripcion[0]
            for descripcion in cursor.description
        ]

        filas = cursor.fetchmany(501)

        if len(filas) > 500:
            filas = filas[:500]
            limitado = True
        else:
            limitado = False

        return {
            "columnas": columnas,
            "filas": filas,
            "total": len(filas),
            "limitado": limitado
        }

    finally:
        conexion.close()


@app.route("/")
def inicio():
    return render_template("index.html", modelo=MODELO)


@app.route("/api/consultar", methods=["POST"])
def consultar():
    datos = request.get_json(silent=True) or {}
    pregunta = str(datos.get("pregunta", "")).strip()

    if not pregunta:
        return jsonify({"error": "Introduce una pregunta."}), 400

    if len(pregunta) > 2000:
        return jsonify({"error": "La pregunta es demasiado larga."}), 400

    try:
        sql = generar_sql(pregunta)
        resultado = ejecutar_sql(sql)

        return jsonify({
            "pregunta": pregunta,
            "sql": sql,
            **resultado
        })

    except requests.RequestException:
        return jsonify({
            "error": "No se ha podido conectar con Ollama."
        }), 502

    except (sqlite3.Error, ValueError) as error:
        return jsonify({
            "error": str(error)
        }), 400


if __name__ == "__main__":
    app.run(debug=True, port=5000)

