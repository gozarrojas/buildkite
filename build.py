import os

file = "build\objeto.txt"

try:
    os.mkdir('build')
except FileExistsError as e:
    print("La carpeta existe")
with open(file,'a') as f:
    f.write("Compilando !!")
    print("He sido creado")
