import os

try:
    os.mkdir('build')
except FileExistsError as e:
    print("La carpeta existe")
with open('build/build.txt','a') as file:
    file.write("Compilando !!")
    print("He sido creado")
