print("Programa en agenda v0.1")
print("por Fernando Puig")

while True:
	print("Escoge una opcion")
	print("1.-Insertar una pelicula")
	print("2.-Listado de peliculas")
	opcion = input("Indica tu opción: ")
	if opcion == "1":
		nombre = input("Introduce un nombre: ")
		director = input("Introduce el director: ")
		año = input("Introduce el año de estreno: ")
		genero= input("Introduce el genero al que pertenece la película")
		archivo = open("peliculas.csv",'a')
		archivo.write(nombre+","+director+","+año+","+genero+"\n")
		archivo.close()
	elif opcion == "2":
		archivo = open("peliculas.csv",'r')
		lineas = archivo.readlines()
		for linea in lineas:
			print(linea)
		archivo.close()	
