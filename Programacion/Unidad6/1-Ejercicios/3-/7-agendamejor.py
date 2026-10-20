agenda = [
    ["Juan", "Perez", "555-111", "Madrid"],     # Fila 0
    ["Ana", "Gomez", "555-222", "Valencia"],    # Fila 1
    ["Luis", "Ruiz", "555-333", "Barcelona"],   # Fila 2
    ["Marta", "Diaz", "555-444", "Sevilla"]     # Fila 3
]

while True:
	print("1-Introducir una persona")
	print("2-Listar agenda")
	opcion=input("Selecciona una opción")
	opcion=int(opcion)
	if opcion == 1: 
		nombre=input("Introduce un nuevo nombre: ")
		apellidos=input("Introduce los apellidos: ")
		email=input("Introduce el email: ")
		agenda.append([nombre,apellidos,email])
	elif opcion == 2:
		print("1-Listar todo")
		print("2-Listar solo nombres")
		opcion_lista=input("Selecciona una opcion")
		opcion_lista=int(opcion_lista)
		if opcion_lista == 1:
			print (agenda)
		elif opcion_lista == 2:
			for linea in agenda:
                		print(linea[0])
					
		


