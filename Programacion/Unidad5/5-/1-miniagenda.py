print("agenda v0.1")
print("por Fernando Puig")

nombre=input("Dime un nombre: ")
apellidos=input("Dime unos apellidos: ")
email=input("Dime un email: ")

archivo=open("agenda.csv",'a')
archivo.write(nombre+","+apellidos+","+email+"\n")
archivo.close()

