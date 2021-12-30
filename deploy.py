import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

file = "build\objeto.txt"
os.mkdir('build')
#Descargamos el artefacto, porque es diferente para cada compilación
os.system('buildkite-agent artifact download "build/objeto.txt" build/')

try:
   with open(file,'a') as f:
       f.write("Desplegando !!")
       print("He sido desplegado")
except FileNotFoundError as e:
    print("El archivo no existe")
