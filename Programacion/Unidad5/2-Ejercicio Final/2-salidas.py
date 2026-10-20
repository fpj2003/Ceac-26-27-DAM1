import tkinter as tk

ventana = tk.Tk()

titulo = tk.Label(ventana,text="Agregador de partidos v0.1")
titulo.pack(padx=20,pady=20)

partido =tk.Label(ventana,text="Introduce el partido")
partido.pack(padx=2,pady=2)

resultado=tk.Label(ventana,text="Introduce el resultado")
resultado.pack(padx=2,pady=2)

competicion=tk.Label(ventana,text="Introduce la competicion")
competicion.pack(padx=2,pady=2)

fecha=tk.Label(ventana,text="Introduce la fecha")
fecha.pack(padx=2,pady=2)

ventana.mainloop()






