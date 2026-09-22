"""
Ejercicio Unidad 1
Calculadora de precio de un viaje
Fernando Puig *

"""

print("Bienvenido al programa, por favor introduzca los datos correspondientes")
kilometros=input("Introduzca los kilometros del viaje")
consumo=input("Introduzca el consumo en litros de su vehiculo por cada 100 km ")
precio=input("Introduzca el precio por litro del combustible ")
pasajeros=input("Introduzca cuantos pasajeros realizaran el viaje")

kilometros=int(kilometros)
consumo=float(consumo)
precio=float(precio)
pasajeros=int(pasajeros)

precio_final=(kilometros*consumo/100)*precio
precio_pasajero= precio_final/pasajeros

print("El precio final de su viaje es de ",precio_final," euros")
print("El precio por cada pasasajero es de ",precio_pasajero,"euros")
