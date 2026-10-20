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



