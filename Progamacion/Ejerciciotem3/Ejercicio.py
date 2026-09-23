"""
Ejercicio Unidad 3 

Fernando Puig

"""
Peliculas=[]
Series=[]
Videojuegos=[]
print("Bienvenido al programa")
while True:
	print("1-Insertar elemento")
	print("2-Ver elementos")
	print("3-Comprobar elementos")
	opcion=input("Elija una opcion")
	opcion=int(opcion)
	
	if opcion == 1:	
		print("Ha seleccionado 'Insertar un elemento' ")
		print("1-Añadir película")
		print("2-Añadir serie")
		print("3-Añadir videojuegos")
		opcion_insertar=input("Elija el elemento a añadir")
		opcion_insertar=int(opcion_insertar)
		if opcion_insertar == 1:
			peli=input("Indica el nombre de la pelicula a añadir")
			Peliculas.append(peli) 
		elif opcion_insertar == 2:
			serie=input("Indica el nombre de la serie a añadir")
			Series.append(serie)
		elif opcion_insertar == 3:
			videojuego=input("Indica el nombre de la pelicula")
			Videjuegos.append(videojuego)
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
    			print(Peliculas)
		elif opcion_ver == 2:
			print("Listado de Series :")
			print(Series)	
    		elif opcion_ver == 3:
			print("Listado de Videojuegos :")
    			print(Videojuegos)
    		elif opcion_ver == 4:	
    			print("Listado de Peliculas, Series y Peliculas :")
    			print("Peliculas:")
    			print(Peliculas)	
			print("Series:")
    			print(Series)
    			print("Videojuegos:")
    			print(Videojuegos)		
	elif opcion == 3:
		print("Ha seleccionado 'Comprobar Elementos' ")
		print("1-Comprobar película")
		print("2-Comprobar series")
		print("3-Comprobar videojuegos")
		opcion_comprobar=input("Elija el elemento a comprobar")
		opcion_comprobar=int(opcion_comprobar)
		if opcion_comprobar == 1:	
			comparador_pelicula = input("Introduce la pelicula a comparar")
			existe_pelicula=False 
			for i in range(len(Peliculas)):
				if Peliculas[i] == comparador_pelicula:
					existe_pelicula=True
			if existe_pelicula == True:
				input("La pelicula ya esta en la lista existe")
			else :
				input("La pelicula no esta en la lista")
		elif opcion_comprobar == 2:	
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
						
