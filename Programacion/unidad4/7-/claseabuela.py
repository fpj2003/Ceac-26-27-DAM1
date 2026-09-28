class Animal()
	def__init__(self):
		self.edad=0
		self.color=""
		self.nombre=""
		
	
class Viviparo(Animal)
	def__init__(self):
		super().__init__()
	def mamar(self)
		return"El animal esta mamando"
		
class Oviparo(Animal)
	def__init__(self):
		super().__init__()
	def reptar(self)
		return"Estoy reptando"
class Perro(Viviparo)	
	def__init__(self):
		super().__init__()
	
	def ladra():
		return "guau"

class Gato(Viviparo)
	def__init__(self):
		super().__init__()
	
	def maulla():
		return "guau"	

class Lagarto(Oviparo):
    def __init__(self):
        super().__init__()
		

mike = Lagarto()
print(micifu.mamar())		
