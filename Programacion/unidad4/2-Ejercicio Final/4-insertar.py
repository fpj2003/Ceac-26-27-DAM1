print("Aplicacion Pilotos v.01")
print("por Fernando Puig")

class Piloto():
	def __init__(self, nombre, apellidos, edad):
		self.nombre=nombre
		self.apellidos=apellidos
		self.edad=edad

class PilotoF1(Piloto):
    def __init__(self, nombre, apellidos, edad, escuderia, dorsal):
        super().__init__(nombre, apellidos, edad)
        self.escuderia = escuderia
        self.dorsal = dorsal

    def listar(self):
        print(f"F1 - {self.nombre} {self.apellidos} | Edad: {self.edad} | Escudería: {self.escuderia} | Dorsal: {self.dorsal}")	
class PilotoF2(Piloto):
    def __init__(self, nombre, apellidos, edad, academia):
        super().__init__(nombre, apellidos, edad)
        self.academia = academia

    def listar(self):
        print(f"F2 - {self.nombre} {self.apellidos} | Edad: {self.edad} | Academia: {self.academia}")    

lista_de_pilotos=[] 

while True:
    print("Escoge una opcion")
    print("1-Insertar un Piloto")
    print("2-Listar Pilotos")
    opcion = input("Indica tu opción: ")
    opcion = int(opcion)

    if opcion == 1:
        print("Has escogido la opción de insertar un piloto")
        print("Selecciona la categoria del piloto")
        print("1- F1")
        print("2- F2")
        opcion_categoria = input("Indica la categoria: ")
        opcion_categoria = int(opcion_categoria)
        if opcion_categoria == 1:
            nombre = input("Introduce el nombre del piloto: ")
            apellidos = input("Introduce los apellidos del piloto: ")
            edad = input("Introduce la edad del piloto: ")
            escuderia = input("Introduce la escuderia del piloto: ")
            dorsal = input("Introduce el dorsal del piloto: ")

            nuevo_piloto = PilotoF1(
                nombre,
                apellidos,
                edad,
                escuderia,
                dorsal
            )
            lista_de_pilotos.append(nuevo_piloto)

        if opcion_categoria == 2:
            nombre = input("Introduce el nombre del piloto: ")
            apellidos = input("Introduce los apellidos del piloto: ")
            edad = input("Introduce la edad del piloto: ")
            academia = input("Introduce la academia del piloto: ")

            nuevo_piloto = PilotoF2(
                nombre,
                apellidos,
                edad,
                academia
            )
            lista_de_pilotos.append(nuevo_piloto)


           
