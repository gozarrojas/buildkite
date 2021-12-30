import os

file = "build/build.txt"
os.mkdir('build')
os.system("buildkite-agent artifact download build/build.txt build/")
try:
   os.path.isfile(file)
   with open(file,'a') as f:
       f.write("Desplegando !!")
       print("He sido desplegado")
except FileNotFoundError as e:
    print("El archivo no existe")
