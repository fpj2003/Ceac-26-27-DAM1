import tkinter as tk

def calcula():
	print("Vamos a calcular")
	kilometro= km.get()
	kilometro = int(kilometro) 
	con = consumo.get()
	con = float(con)
	litro = litros.get()
	litro= float(litro)
	pasajero = pasajeros.get()
	pasajero = int(pasajero)
	precio_final=(kilometro*con/100)*litro
	precio_pasajero= precio_final/pasajero
	resultado1.config(text=precio_final)	
	resultado2.config(text=precio_pasajero)

ventana = tk.Tk()
ventana.geometry("600x400")

etiqueta = tk.Label(text="Introduzca los kilometros del viaje")
etiqueta.pack(padx=10,pady=10)

km = tk.Entry()
km.pack(padx=10,pady=10)

etiqueta = tk.Label(text="Introduzca el consumo en litros de su vehiculo por cada 100 km ")
etiqueta.pack(padx=10,pady=10)

consumo = tk.Entry()
consumo.pack(padx=10,pady=10)

etiqueta = tk.Label(text="Introduzca el precio por litro del combustible ")
etiqueta.pack(padx=10,pady=10)

litros = tk.Entry()
litros.pack(padx=10,pady=10)

etiqueta = tk.Label(text="Introduzca el número de pasajeros ")
etiqueta.pack(padx=10,pady=10)

pasajeros = tk.Entry()
pasajeros.pack(padx=10,pady=10)



# Dispara la acción
boton = tk.Button(text="Vamos a calcular",command=calcula)
boton.pack(padx=10,pady=10)

# Solemos usar label para sacar el resultado
resultado1 = tk.Label(text="Precio final")
resultado1.pack(padx=10,pady=10)

resultado2 = tk.Label(text="Precio final de cada pasajero")
resultado2.pack(padx=10,pady=10)
ventana.mainloop() # no te salgas, bucle infinito
