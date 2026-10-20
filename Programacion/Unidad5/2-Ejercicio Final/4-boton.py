import tkinter as tk

ventana = tk.Tk()

titulo = tk.Label(ventana,text="Agregador de partidos v0.1")
titulo.pack(padx=20,pady=20)

partido =tk.Label(ventana,text="Introduce el partido")
partido.pack(padx=2,pady=2)
inputpartido=tk.Entry(ventana)
inputpartido.pack(padx=20,pady=20)

resultado=tk.Label(ventana,text="Introduce el resultado")
resultado.pack(padx=2,pady=2)
inputresultado=tk.Entry(ventana)
inputresultado.pack(padx=20,pady=20)


competicion=tk.Label(ventana,text="Introduce la competicion")
competicion.pack(padx=2,pady=2)
inputcompeticion=tk.Entry(ventana)
inputcompeticion.pack(padx=20,pady=20)

fecha=tk.Label(ventana,text="Introduce la fecha")
fecha.pack(padx=2,pady=2)
inputfecha=tk.Entry(ventana)
inputfecha.pack(padx=20,pady=20)

boton=tk.Button(ventana,text="Inserta partido")
boton.pack(padx=20,pady=20)

ventana.mainloop()







