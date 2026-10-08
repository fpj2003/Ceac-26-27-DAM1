
def encriptar(entrada):
	salida=""
	for letra  in entrada:
		salida+=chr(ord(letra)+5)
	return salida
	
def desencriptar(entrada):
	salida=""
	for letra  in entrada:
		salida+=chr(ord(letra)-5)
	return salida

cadena=("Fernando")
encriptado=encriptar(cadena)
desencriptado=desencriptar(encriptado)

print(encriptado)
print(desencriptado)

