class Persona():
  def __init__(self,minombre):
    self.nombre = minombre
    self.emails = []
    
persona1 = Persona("Fernando")
persona1.emails.append("fpj@gmail.com")
persona1.emails.append("ferpuig@gmail.com")

print(persona1)
