import ttkbootstrap as tb
from ttkbootstrap.constants import *
import tkinter as tk # Aún lo usamos para la constante tk.END en el Text

# Cambiamos tk.Tk() por tb.Window y elegimos un tema (puedes probar "darkly", "cosmo", "cyborg")
ventana = tb.Window(themename="superhero")
ventana.title("Gestor de Partidos Deportivos")
ventana.geometry("850x650")

def insertaPartido():
    Equipolocal = inputequipolocal.get()
    Equipovisitante = inputequipovisitante.get()
    Resultado = inputresultado.get()
    Competicion = inputcompeticion.get()
    Fecha = inputfecha.get()
    
    # Guardar en archivo
    with open("partidos.csv", "a") as archivo:
        archivo.write(f"{Equipolocal} {Resultado} {Equipovisitante},{Competicion},{Fecha}\n")
    
    # Refrescar el campo de texto
    campodetexto.delete("1.0", tk.END)
    with open("partidos.csv", "r") as archivo:
        for linea in archivo.readlines():
            campodetexto.insert(tk.END, linea)
            
    # Limpiar las cajas de texto tras insertar
    inputequipolocal.delete(0, END)
    inputequipovisitante.delete(0, END)
    inputresultado.delete(0, END)
    inputcompeticion.delete(0, END)
    inputfecha.delete(0, END)

# Marco principal con padding para que respire el diseño
marco = tb.Frame(ventana, padding=20)
marco.grid(row=0, column=0, sticky="nsew")

# Título con fuente más grande y estilo del tema
titulo = tb.Label(marco, text="Agregador de partidos v0.2", font=("Helvetica", 16, "bold"), bootstyle="primary")
titulo.pack(pady=(0, 20))

# Campos de formulario con estilos 'info'
equipolocal = tb.Label(marco, text="Equipo local")
equipolocal.pack(fill=X, pady=(5, 2))
inputequipolocal = tb.Entry(marco, bootstyle="info")
inputequipolocal.pack(fill=X, pady=(0, 10))

equipovisitante = tb.Label(marco, text="Equipo visitante")
equipovisitante.pack(fill=X, pady=(5, 2))
inputequipovisitante = tb.Entry(marco, bootstyle="info")
inputequipovisitante.pack(fill=X, pady=(0, 10))

resultado = tb.Label(marco, text="Resultado")
resultado.pack(fill=X, pady=(5, 2))
inputresultado = tb.Entry(marco, bootstyle="info")
inputresultado.pack(fill=X, pady=(0, 10))

competicion = tb.Label(marco, text="Competición")
competicion.pack(fill=X, pady=(5, 2))
inputcompeticion = tb.Entry(marco, bootstyle="info")
inputcompeticion.pack(fill=X, pady=(0, 10))

fecha = tb.Label(marco, text="Fecha")
fecha.pack(fill=X, pady=(5, 2))
inputfecha = tb.Entry(marco, bootstyle="info")
inputfecha.pack(fill=X, pady=(0, 20))

# Botón con estilo 'success' (verde) y contorno
boton = tb.Button(marco, text="Inserta partido", command=insertaPartido, bootstyle="success-outline")
boton.pack(fill=X, pady=10)

# Campo de texto lateral
campodetexto = tb.Text(ventana, width=40, font=("Helvetica", 10))
campodetexto.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

# Configurar el peso de las columnas para que se expanda bien si cambias el tamaño de la ventana
ventana.columnconfigure(1, weight=1)
ventana.rowconfigure(0, weight=1)

# Cargar datos previos al abrir el programa por primera vez
try:
    with open("partidos.csv", "r") as archivo:
        for linea in archivo.readlines():
            campodetexto.insert(tk.END, linea)
except FileNotFoundError:
    pass # Si el archivo no existe aún, no hace nada

ventana.mainloop()
