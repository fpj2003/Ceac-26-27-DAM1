class Animal()
	def__init__(self):
		self.edad=0
		self.color=""
		self.nombre=""
	def mamar(self)
		return"El animal esta mamando"	
	
class Perro(Animal)	
	def__init__(self):
		super().__init__()
	
	def ladra():
		return "guau"

class Gato(Animal)
	def__init__(self):
		super().__init__()
	
	def maulla():
		return "guau"	

class Lagarto(Animal):
    def __init__(self):
        super().__init__()
		

mike = Lagarto()
print(micifu.mamar())		
