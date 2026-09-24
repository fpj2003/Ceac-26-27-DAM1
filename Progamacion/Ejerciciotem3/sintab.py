"""
Ejercicio Unidad 3 

Fernando Puig

"""
#DECLARACION DE LISTAS
Peliculas=[]
Series=[]
Videojuegos=[]

#ENTRADAS Y MENU DEL PROGRAMA
print("Bienvenido al programa")
while True:											#BUCLE PARA MANTENER EL PROGRAMA ACTIVO
	print("1-Insertar elemento")
	print("2-Ver elementos")
	print("3-Comprobar elementos")
	opcion=input("Elija una opcion")							##EL USUARIO ELIGE QUE OPCION EJECUTAR Y LO GUARDA EN LA VARIABLE OPCION
	opcion=int(opcion)									#SE CONVIERTE LA VARIABLE OPCION A INT
												#DEPENDIENDO DEL NUMERO INTRODUCIDO SE EJECUTARA UNA OPCION					
#MENU DE LA OPCION DE INSERTAR
	if opcion == 1:										
		print("Ha seleccionado 'Insertar un elemento' ") 				#DENTRO DE CADA OPCION HAY 3 SUBOPCIONES PARA MODIFICAR UNA LISTA DIFERENTE
		print("1-Añadir película")
		print("2-Añadir serie")
		print("3-Añadir videojuegos")
		opcion_insertar=input("Elija el elemento a añadir")				#EL USUARIO ELIGE QUE SUBOPCION EJECUTAR
		opcion_insertar=int(opcion_insertar)
		if opcion_insertar == 1:
			peli=input("Indica el nombre de la pelicula a añadir")			#GUARDA EL NOMBRE DE LA PELICULA EN UNA VARIABLE				
			Peliculas.append(peli)							#GUARDA LA PELICULA EN LA LISTA 
		elif opcion_insertar == 2:
			serie=input("Indica el nombre de la serie a añadir")			#SE REPITEN LOS MISMOS PASOS PARA SERIES Y VIDEOJUEGOS
			Series.append(serie)
		elif opcion_insertar == 3:							
			videojuego=input("Indica el nombre de la pelicula")
			Videojuegos.append(videojuego)

#MENU DE LA OPCION DE LISTAR
	elif opcion == 2:									
		print("Ha seleccionado 'Listar Elementos' ")
		print("1-Ver las película")
		print("2-Ver las series")
		print("3-Ver los videojuegos")
		print("4-Ver todos los elementos")
		opcion_ver=input("Elija el elemento a ver")
		opcion_ver=int(opcion_ver)
		if opcion_ver == 1:						
			print("Listado de Peliculas :")
			print(Peliculas)							#IMPRIME POR PANTALLA EL CONTENIDO DE LA LISTA PELICULA
		elif opcion_ver == 2:
			print("Listado de Series :")
			print(Series)								#IMPRIME POR PANTALLA EL CONTENIDO DE LA LISTA SERIES
		elif opcion_ver == 3:
			print("Listado de Videojuegos :")
			print(Videojuegos)							#IMPRIME POR PANTALLA EL CONTENIDO DE LA LISTA VIDEOJUEGOS
		elif opcion_ver == 4:
			print("Listado de Peliculas, Series y Peliculas :")			#IMPRIME POR PANTALLA EL CONTENIDO DE TODAS LAS LISTAS 
			print("Peliculas:")
			print(Peliculas)
			print("Series:")
			print(Series)
			print("Videojuegos:")
			print(Videojuegos)
			
#MENU DE LA OPCION DE COMPROBAR	
	elif opcion == 3:
		print("Ha seleccionado 'Comprobar Elementos' ")
		print("1-Comprobar película")
		print("2-Comprobar series")
		print("3-Comprobar videojuegos")
		opcion_comprobar=input("Elija el elemento a comprobar")
		opcion_comprobar=int(opcion_comprobar)
		if opcion_comprobar == 1:
			comparador_pelicula = input("Introduce la pelicula a comparar")
			existe_pelicula=False							#SE CREA UNA VARIABLE BOOLEANA FALSE 
			for i in range(len(Peliculas)):						#A TRAVES DEL FOR SE RECORRE LA LISTA, OBTENIENDO SU TAMAÑO CON LEN,DE MANERA QUE RECORRA TODA LA LISTA SIENDO DEL TAMAÑO QUE SEA
				if Peliculas[i] == comparador_pelicula:				#COMPRUEBA QUE LA PELICULA QUE SE HA INTRODUCIDO SE ENCUENTRA EN LA LISTA
					existe_pelicula=True					#SI SE ENCUENTRA EN LA LISTA EL VALOR DE LA VARIABLE BOOLEANA SE VUELVE TRUE
			if existe_pelicula == True:						#COMPRUEBA QUE LA VARIABLE BOOLEANA SEA TRUE, SI LO ES DEVOLVERA QUE LA PELICULA EXISTE
				input("La pelicula ya esta en la lista existe")
			else :									#SI LA VARIABLE BOOLEANA ES FALSA, SIGINFICARA QUE NO HA ENCONTRADO LA PELICULA POR LO TANTO 
				input("La pelicula no esta en la lista")			#DEVUELVE QUE EXISTE
		elif opcion_comprobar == 2:							#SE REPITEN LOS MISMO PASOS PARA COMPROBAR SERIES Y VIDEOJUEGOS
			comparador_serie = input("Introduce la serie a comparar")
			existe_serie=False
			for i in range(len(Series)):
				if Series[i] == comparador_serie:
					existe_serie=True
			if existe_serie == True:
				input("La pelicula ya esta en la lista existe")
			else :
				input("La pelicula no esta en la lista")
		elif opcion_comprobar == 3:
			comparador_videojuego = input("Introduce el videojuego a comparar")
			existe_videojuego=False
			for i in range(len(Videojuegos)):
				if Videojuegos[i] == comparador_videojuego:
					existe_videojuego=True
			if existe_videojuego == True:
				input("La pelicula ya esta en la lista existe")
			else :
				input("La pelicula no esta en la lista")
