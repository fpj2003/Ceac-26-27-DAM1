import tkinter as tk

ventana = tk.Tk()

def insertaPartido():
	print("Voy a insertar un partido")
	Equipolocal=inputequipolocal.get()
	Equipovisitante=inputequipovisitante.get()
	Resultado=inputresultado.get()
	Competicion=inputcompeticion.get()
	Fecha=inputfecha.get()
	archivo=open("partidos.csv","a")
	archivo.write(Equipolocal+" "+Resultado+" "+Equipovisitante+","+Competicion+","+Fecha+"\n")
	archivo.close()
	campodetexto.delete("1.0",tk.END)
	archivo=open("partidos.csv","r")
	lineas=archivo.readlines()
	for linea in lineas:
		campodetexto.insert(tk.END,linea)
	archivo.close()
	
marco = tk.Frame(ventana)

titulo = tk.Label(marco,text="Agregador de partidos v0.1")
titulo.pack(padx=20,pady=20)

equipolocal =tk.Label(marco,text="Introduce el equipo local")
equipolocal.pack(padx=2,pady=2)
inputequipolocal=tk.Entry(marco)
inputequipolocal.pack(padx=20,pady=20)

equipovisitante =tk.Label(marco,text="Introduce el equipo visitante")
equipovisitante.pack(padx=2,pady=2)
inputequipovisitante=tk.Entry(marco)
inputequipovisitante.pack(padx=20,pady=20)

resultado=tk.Label(marco,text="Introduce el resultado")
resultado.pack(padx=2,pady=2)
inputresultado=tk.Entry(marco)
inputresultado.pack(padx=20,pady=20)


competicion=tk.Label(marco,text="Introduce la competicion")
competicion.pack(padx=2,pady=2)
inputcompeticion=tk.Entry(marco)
inputcompeticion.pack(padx=20,pady=20)

fecha=tk.Label(marco,text="Introduce la fecha")
fecha.pack(padx=2,pady=2)
inputfecha=tk.Entry(marco)
inputfecha.pack(padx=20,pady=20)

boton=tk.Button(marco,text="Inserta partido",command=insertaPartido)
boton.pack(padx=20,pady=20)

marco.grid(row=0,column=0)

campodetexto = tk.Text(ventana)
campodetexto.grid(row=0,column=1,padx=20,pady=20)

ventana.mainloop()

