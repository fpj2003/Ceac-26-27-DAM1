import os

directorio= "/home/fernando/Programacion"

for x,y,z in os.walk(directorio):
  print(x)
  print(y)
  print(z)
