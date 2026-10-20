import tkinter as tk

ventana = tk.Tk()
ventana.geometry("600x400")

etiqueta = tk.Label(text="Hola mundo en Tkinter")
etiqueta.pack()

boton= tk.Button(text="Pulsame si te atreves")
boton.pack()

ventana.mainloop() # no te salgas, bucle infinito
