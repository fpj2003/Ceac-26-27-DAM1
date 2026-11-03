class Tornillo:
	def __init__(self,mi_radio):
		radio = mi_radio
		tornillo1 = Tornillo(5)
class Rueda:
	def __init__(self,mi_radio):
		radio=mi_radio
class Motor:
	def __init(self,minicilindrada,caballos):
		cilindrada = minicilindrada
		potencia = caballos		
class Coche:
	def __init__(self,combustible,ada,cv,micolor):
		tipocombustible = combustible
		sistema_ada = ada
		motor = Motor(100,45)
		rueda = Rueda(21)
		color = micolor
	def arrancar(self):
		return "El coche ha arrancado"
	def acelerar(self):
		return"El coche ha acelerado"		

micoche = Coche("gasolina",True,"rojo")		
