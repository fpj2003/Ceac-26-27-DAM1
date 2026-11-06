from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculadora_iva():
    base_imponible = None
    iva = None
    total = None

    if request.method == "POST":
        try:
            base_imponible = float(request.form["base_imponible"])
            porcentaje_iva = float(request.form["porcentaje_iva"])
            iva = base_imponible * porcentaje_iva / 100
            total = base_imponible + iva
        except ValueError:
            pass

    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Calculadora de IVA</title>
        <style>
            /* Estilos CSS aquí */
        </style>
    </head>
    <body>
        <h1>Calculadora de IVA</h1>
        <form method="POST">
            <label for="base_imponible">Base imponible:</label>
            <input type="number" name="base_imponible" required>
            <label for="porcentaje_iva">Porcentaje de IVA:</label>
            <select name="porcentaje_iva">
                <option value="4">4%</option>
                <option value="10">10%</option>
                <option value="21">21%</option>
            </select>
            <button type="submit">Calcular</button>
        </form>
        {% if base_imponible and iva and total %}
        <p>Base imponible: {{ base_imponible }}</p>
        <p>IVA: {{ iva }}</p>
        <p>Total: {{ total }}</p>
        {% endif %}
    </body>
    </html>
    """

    return render_template_string(html, base_imponible=base_imponible, iva=iva, total=total)

if __name__ == "__main__":
    app.run(debug=True)
