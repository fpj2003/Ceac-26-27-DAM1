
import requests
import re

ruta = "http://localhost:11434/api/generate"
modelo = "qwen2.5-coder:7b"

pregunta = """
Eres un generador automático de código Python.

Tu respuesta será guardada DIRECTAMENTE en un archivo llamado
miprograma.py y ejecutada mediante Python.

REGLAS OBLIGATORIAS:

1. Genera EXACTAMENTE UN ÚNICO ARCHIVO Python.
2. Toda la aplicación debe estar contenida en ese archivo.
3. Está TERMINANTEMENTE PROHIBIDO generar archivos adicionales.
4. NO generes carpetas templates ni static.
5. NO utilices render_template ni render_template_string
   con archivos externos.
6. El HTML debe estar embebido en una cadena multilínea
   dentro del propio archivo Python.
7. El CSS debe estar dentro de una etiqueta style
   en el HTML embebido.
8. El JavaScript, si lo necesitas, también debe estar embebido.
9. Utiliza Flask para crear el servidor web.
10. La aplicación debe arrancar mediante:
    if __name__ == "__main__":
        app.run(debug=True)
11. Incluye todos los imports necesarios.
12. No incluyas comentarios ni explicaciones.
13. No incluyas instrucciones de instalación.
14. No incluyas nombres de archivos ni separadores.
15. No incluyas Markdown.
16. No utilices fences de código.
17. No escribas ```python ni ```.
18. No escribas texto antes ni después del código.
19. La primera línea debe ser código Python válido.
20. El resultado debe poder guardarse directamente
    como miprograma.py y ejecutarse.

TAREA:

Crea una calculadora de IVA mediante Flask.

REQUISITOS:

- Interfaz web moderna y visualmente atractiva.
- HTML y CSS embebidos en el archivo Python.
- Formulario para introducir una cantidad.
- Selector de IVA: 4%, 10% y 21%.
- Calcular base imponible, IVA y total.
- Mostrar los resultados en la misma página.
- Validar las entradas del usuario.
- Diseño responsive.
- Todo en un único archivo Python.

IMPORTANTE:
Tu salida será escrita literalmente en un archivo .py.
Cualquier texto que no sea Python invalidará el programa.

DEVUELVE ÚNICAMENTE CÓDIGO PYTHON EJECUTABLE.
"""

respuesta = requests.post(
    ruta,
    json={
        "model": modelo,
        "prompt": pregunta,
        "stream": False,
        "options": {
            "temperature": 0.1,
            "num_predict": 4096
        }
    },
    timeout=300
)

respuesta.raise_for_status()

codigo = respuesta.json()["response"].strip()

# Eliminar fences de Markdown si aparecen
codigo = re.sub(
    r"^\s*```(?:python|py)?\s*\n",
    "",
    codigo,
    flags=re.IGNORECASE
)

codigo = re.sub(
    r"\n?\s*```\s*$",
    "",
    codigo
)

codigo = codigo.strip()

# Comprobar que el código tiene sintaxis Python válida
compile(codigo, "miprograma.py", "exec")

# Guardar únicamente si supera la validación
with open("miprograma.py", "w", encoding="utf-8") as archivo:
    archivo.write(codigo + "\n")

print("Archivo miprograma.py generado correctamente.")

