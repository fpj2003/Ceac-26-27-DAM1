nombre="Fernando"
def encriptar(entrada):
	salida=""
	for letra  in entrada:
		salida+=chr(ord(letra)+5)
	return salida
print(encriptar("Fernando"))
print(encriptar("Esto es una frase de prueba que estoy encriptando"))	
