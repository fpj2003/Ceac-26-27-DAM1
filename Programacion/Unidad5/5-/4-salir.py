
print("agenda v0.1")
print("por Fernando Puig")



while True:
	print("Escoge una opcion:")
	print("1.-Insertar datos")
	print("2.-Leer datos")
	print("3-Salir")
	opcion = input("Escoge una opción: ")	
	if opcion == "1":
		nombre=input("Dime un nombre: ")
		apellidos=input("Dime unos apellidos: ")
		email=input("Dime un email: ")
		archivo=open("agenda.csv",'a')
		archivo.write(nombre+","+apellidos+","+email+"\n")
		archivo.close()
	if opcion == "2":
		archivo = open("agenda.csv",'r')
		lineas = archivo.readlines()
		for linea in lineas:
			print(linea)
		archivo.close()
	elif opcion == "3":
		exit()
