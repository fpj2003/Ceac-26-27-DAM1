"""
Ejercicio Unidad 3 
Lista de Películas ,Series y videojuegos
Fernando Puig

"""
#DECLARACION DE LISTAS
Peliculas=[]
Series=[]
Videojuegos=[]

#ENTRADAS Y MENU DEL PROGRAMA
print("Bienvenido al programa")
while True:											                                #BUCLE PARA MANTENER EL PROGRAMA ACTIVO
	print("1-Insertar elemento")
	print("2-Ver elementos")
	print("3-Comprobar elementos")
	opcion=input("Elija una opcion")							                    #EL USUARIO ELIGE QUE OPCION EJECUTAR Y LO GUARDA EN LA VARIABLE OPCION		
	opcion=int(opcion)		                                                        #SE CONVIERTE LA VARIABLE OPCION A INT, DEPENDIENDO DEL NUMERO INTRODUCIDO SE EJECUTARA UNA OPCION
			
		
	#MENU DE LA OPCION DE INSERTAR
	
	if opcion == 1:	
		print(30*'-')												                #IMPRIME UNA LINEA DE GUIONES PARA SEPARAR EL MENU DE LA OPCION ELEGIDA
		print("Ha seleccionado 'Insertar un elemento' ") 			                #DENTRO DE CADA OPCION HAY 3 SUBOPCIONES PARA MODIFICAR UNA LISTA DIFERENTE
		print("1-Añadir película")
		print("2-Añadir serie")
		print("3-Añadir videojuegos")
		opcion_insertar=input("Elija el elemento a añadir")			                #EL USUARIO ELIGE QUE SUBOPCION EJECUTAR
		opcion_insertar=int(opcion_insertar)
		if opcion_insertar == 1:
			peli=input("Indica el nombre de la pelicula a añadir")		            #GUARDA EL NOMBRE DE LA PELICULA EN UNA VARIABLE				
			Peliculas.append(peli)						                            #GUARDA LA PELICULA EN LA LISTA 
		elif opcion_insertar == 2:
			serie=input("Indica el nombre de la serie a añadir")		            #SE REPITEN LOS MISMOS PASOS PARA SERIES Y VIDEOJUEGOS
			Series.append(serie)
		elif opcion_insertar == 3:							
			videojuego=input("Indica el nombre del videojuego a añadir")
			Videojuegos.append(videojuego)
		
		print(30*'-')

#MENU DE LA OPCION DE LISTAR
		
	elif opcion == 2:									
		print(30*'-')											
		print("Ha seleccionado 'Listar Elementos' ")
		print("1-Ver las película")
		print("2-Ver las series")
		print("3-Ver los videojuegos")
		print("4-Ver todos los elementos")
		opcion_ver=input("Elija el elemento a ver")
		opcion_ver=int(opcion_ver)
		if opcion_ver == 1:						
			print("Listado de Peliculas :")
			print(Peliculas)						                                #IMPRIME POR PANTALLA EL CONTENIDO DE LA LISTA PELICULA
		elif opcion_ver == 2:
			print("Listado de Series :")
			print(Series)							                                #IMPRIME POR PANTALLA EL CONTENIDO DE LA LISTA SERIES
		elif opcion_ver == 3:
			print("Listado de Videojuegos :")
			print(Videojuegos)						                                #IMPRIME POR PANTALLA EL CONTENIDO DE LA LISTA VIDEOJUEGOS
		elif opcion_ver == 4:
			print("Listado de Peliculas, Series y Videojuegos :")                   #IMPRIME POR PANTALLA EL CONTENIDO DE TODAS LAS LISTAS 
			print("Peliculas:")
			print(Peliculas)
			print("Series:")
			print(Series)
			print("Videojuegos:")
			print(Videojuegos)
		print(30*'-')		