edad=input("Introudce tu edad") 
edad=int(edad)

if edad < 10:
 	print("Eres un niño")
 
elif edad < 20:
	print ("Eres un adolescente")
	
elif edad < 30:
	print ("Eres un joven")	
	
elif edad >=30 and edad < 40:
	print ("Eres un adolescente")	
else :
	print("Eres un viejo")	
