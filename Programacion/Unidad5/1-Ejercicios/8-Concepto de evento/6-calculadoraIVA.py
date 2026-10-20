import tkinter as tk

def calcula():
	print("Vamos a calcular")
	base_imp = base.get()
	base_imp = float(base_imp) 
	iva = base_imp*0.21
	resultado.config(text=iva)

ventana = tk.Tk()
ventana.geometry("600x400")

etiqueta = tk.Label(text="Dime la base imponible")
etiqueta.pack(padx=10,pady=10)

base = tk.Entry()
base.pack(padx=10,pady=10)

# Dispara la acción
boton = tk.Button(text="Vamos a calcular el IVA",command=calcula)
boton.pack(padx=10,pady=10)

# Solemos usar label para sacar el resultado
resultado = tk.Label(text="Resultado")
resultado.pack(padx=10,pady=10)

ventana.mainloop() # no te salgas, bucle infinito




