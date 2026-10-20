import tkinter as tk

ventana = tk.Tk()
ventana.geometry("600x400")

etiqueta = tk.Label(text="Operando 1")
etiqueta.pack()

operando1= tk.Entry()
operando1.pack(padx=10,pady=10)

etiqueta = tk.Label(text="Operando 2")
etiqueta.pack()

operando2= tk.Entry()
operando2.pack(padx=20,pady=20)

boton = tk.Button(text="Vamos a calcular")
boton.pack(padx=10,pady=10)

resultado = tk.Label(text="Resultado")
resultado.pack(padx=10,pady=10)

ventana.mainloop() # no te salgas, bucle infinito
