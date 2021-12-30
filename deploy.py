import os

file = "build.txt"
os.mkdir('build')
os.system("buildkite-agent artifact download build/build.txt build/")
try:
   os.path.isfile(file)
   with open("build/"+file,'a') as f:
       f.write("Desplegando !!")
       print("He sido desplegado")
except FileNotFoundError as e:
    print("El archivo no existe")
