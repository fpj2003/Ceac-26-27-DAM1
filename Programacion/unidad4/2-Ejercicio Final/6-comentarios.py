print("Aplicacion Pilotos v.01")
print("por Fernando Puig")

#CREO LA CLASE MADRE PILOTO
class Piloto():
	def __init__(self, nombre, apellidos, edad):        #CONTRUCTOR DE LA CLASE PILOTO
		self.nombre=nombre
		self.apellidos=apellidos
		self.edad=edad

#CREO LAS CLASES HIJAS PILOTO F1 Y PILOTO F2
class PilotoF1(Piloto):
    def __init__(self, nombre, apellidos, edad, escuderia, dorsal): #CREO EL CONSTRUCTOR DE LA CLASE PILOTO F1
        super().__init__(nombre, apellidos, edad)
        self.escuderia = escuderia
        self.dorsal = dorsal

    def listar(self):                                               #CREO METODO PARA PODER LISTAR LOS PILOTOS DE F1
        print(f"F1 - {self.nombre} {self.apellidos} | Edad: {self.edad} | Escudería: {self.escuderia} | Dorsal: {self.dorsal}")	

#CREO LA CLASE HIJA PILOTO F2
class PilotoF2(Piloto):
    def __init__(self, nombre, apellidos, edad, academia):  #CREO EL CONSTRUCTOR DE LA CLASE PILOTO F2
        super().__init__(nombre, apellidos, edad)
        self.academia = academia

    def listar(self):                       #CREO METODO PARA PODER LISTAR LOS PILOTOS DE F2
        print(f"F2 - {self.nombre} {self.apellidos} | Edad: {self.edad} | Academia: {self.academia}")    

lista_de_pilotos=[]     #CREO UNA LISTA VACIA PARA PODER ALMACENAR LOS PILOTOS


while True:             #CREO UN BUCLE INFINITO COMO MENU DEL PROGRAMA                                                
    print("Escoge una opcion")
    print("1-Insertar un Piloto")
    print("2-Listar Pilotos")
    opcion = input("Indica tu opción: ")
    opcion = int(opcion)

    #OPCION PARA INSERTAR UN PILOTO
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
    
    
    #OPCION PARA LISTAR LOS PILOTOS
    if opcion == 2:
        print("Has escogido la opción de listar pilotos")
        for piloto in lista_de_pilotos:     #CREO BLUCE FOR PARA RECORRER LA LISTA DE PILOTOS Y MENDIANTE EL METODO DE LISTAR SE MUESTRAN LOS PILOTOS
            print("-"*30)
            piloto.listar()
