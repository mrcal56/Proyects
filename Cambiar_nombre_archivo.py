import os

actualDir= os.getcwd()
print(actualDir)
dir = input("Directorio al que quieres ir: ")

usuarioDir =  os.chdir(dir)
print(actualDir)
listar = os.listdir(usuarioDir)
print("Estos son los archivos del directorio",listar)

eliminar = 
