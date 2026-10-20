import os

directorio = "/home/fernando/Programacion"

for x,y,z in os.walk(directorio):
  print(x)

for x,y,z in os.walk(directorio):
  print(y)
  
for x,y,z in os.walk(directorio):
  print(z)

