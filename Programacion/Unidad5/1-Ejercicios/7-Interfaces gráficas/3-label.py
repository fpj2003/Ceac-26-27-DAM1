import tkinter as tk

ventana = tk.Tk()
ventana.geometry("600x400")

etiqueta = tk.Label(text="Hola mundo en Tkinter")
etiqueta.pack()

ventana.mainloop() # no te salgas, bucle infinito
