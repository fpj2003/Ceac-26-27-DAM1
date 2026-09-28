#Bienvenida
print("Aplicacion Hospital v.01")
print("por Fernando Puig")

#Defino paciente
class Persona():
	def __init__(self,nombre,apellidos,email):
		self.nombre=""
		self.apellidos=""
		self.email=""
class Paciente(Persona):
	def __init__(self,nombre,apellidos,email):
		super().__init__(nombre,apellidos,email)
#Creo lista de clientes		
lista_de_pacientes=[]	

while True:
	print("Escoge una opcion")
	print("1-Insertar un Paciente")
	print("2-Listar Pacientes")
	opcion = input("Indica tu opción: ")
	if opcion == "1":
		print("Ahora vemos como insertamos un paciente")
		nombre=input("Introduce el nombre del cliente:")
		apellidos=input("Introduce los apellidos del cliente:")
		email=input("Introduce el email del paciente")
	if opcion == "2":
		print("Ahora listamos los pacientes")	
		for paciente in lista_de_pacientes:
			print("-"*30)
			print(paciente.nombre)
			print(paciente.apellidos)
			print(paciente.email)
			print("-"*30)
	else:
    		print("opción no reconocida")
    
