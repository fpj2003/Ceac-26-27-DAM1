
print("Aplicacion Hospital v.01")
print("por Fernando Puig")


class Paciente():
	def __init__(self,nombre,apellidos,email):
		self.nombre=""
		self.apellidos=""
		self.email=""


lista_de_pacientes=[]	

while True:
	print("Escoge una opcion")
	print("1-Insertar un Paciente")
	print("2-Listar Pacientes")
	opcion = input("Indica tu opción: ")
