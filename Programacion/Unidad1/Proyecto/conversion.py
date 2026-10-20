"""
Ejercicio Unidad 1
Calculadora de precio de un viaje
Fernando Puig *

"""
#BIENVENIDA AL PROGRAMA Y ENTRADA DE INFORMACION
print("Bienvenido al programa, por favor introduzca los datos correspondientes")	#Salida
kilometros=input("Introduzca los kilometros del viaje")					#Entrada de variables
consumo=input("Introduzca el consumo en litros de su vehiculo por cada 100 km ")
precio=input("Introduzca el precio por litro del combustible ")
pasajeros=input("Introduzca cuantos pasajeros realizaran el viaje")

#CONVERTIR LAS VARIABLES A LAS NECESARIAS PARA OPERAR
kilometros=int(kilometros)	#Convierto a entero			
consumo=float(consumo)		#Convierto a float
precio=float(precio)		#Convierto a float
pasajeros=int(pasajeros)	#Convierto a entero
