print("Programa lista de la compra")
lista_de_la_compra= []

while True:
	print("Escoge una opcion")
	print("1-Insertar nuevo elemento")
	print("2-Listar elementos")
	print("3-Comprueba que ese objeto existe")
	
	opcion = input("Escoge una opcion")
	if opcion == "1":
		elemento = input("Introduce un nuevo elemento")
		lista_de_la_compra.append(elemento)
	elif opcion == "2":
		print(lista_de_la_compra)
	elif opcion == "3":
		comparador = input("Introduce el objeto a comparar")
		existe=False 
		for i in range(len(lista_de_la_compra)):
			if lista_de_la_compra[i] == comparador:
				existe=True
		if existe == True:
			input("El objeto existe")
		else :
			input("El objeto no existe")

