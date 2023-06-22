import os
import subprocess

def nuevo_usuario():
    confirmar = "N"
    nombre_usuario = ""
    
    while confirmar != "S":
        nombre_usuario = input("Ingrese el nombre del usuario que desea agregar: ")
        print("¿Desea utilizar el nombre '" + nombre_usuario + "'? (S/N)")
        confirmar = input().upper()
    
    os.system("sudo adduser " + nombre_usuario)

def elimina_usuario():
    confirmar = "N"
    nombre_usuario = ""
    
    while confirmar != "S":
        nombre_usuario = input("Ingrese el nombre del usuario que desea eliminar: ")
        print("¿Desea eliminar el usuario'" + nombre_usuario + "'? (S/N)")
        confirmar = input().upper()
    
nombre_usuario="jabermudez"  
comando= ["sudo", "id", nombre_usuario]
resultado=subprocess.run(comando,capture_output=True, text=True)    
if resultado.returncode == 0:
    salida = resultado.stdout
    print(salida)
else:
    error = resultado.stderr
    print(f"Se produjo un error: {error}")
