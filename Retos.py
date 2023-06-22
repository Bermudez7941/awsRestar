"""ValUser=int(input("ingrese su valor "))

if ValUser % 2 ==0:
    print("El valor es par")
else:
   print("El valor es impar") """


"""ValUser=input("ingrese su contraseña ")
Contraseña="2020"
if ValUser==Contraseña:
    print("Contraseña valida")
else:
   print("Contraseña invalida")"""

"""ValUser=int(input("ingrese su numero "))
i=-1
while i < ValUser:
    print(ValUser)
    ValUser -= 1"""

"""ValUser=int(input("ingrese su numero "))
numero=8
while numero != ValUser:
    print("No adivinaste")
    ValUser=int(input("Ingrese otor numero "))
print("Adivinaste")"""

"""Userini = int(input("Ingrese el número inicial: "))
Userfin = int(input("Ingrese el número final: "))
suma = 02
for numero in range(Userini, Userfin + 1):
    suma += numero
print("El valor total es:", suma)"""

import random
number = random.randint(1,10)
correcto = False
while correcto is False:
    trial = int(input("Ingrese numero:"))
    if trial == number:
        print("Felicidades, numero correcto!")
        correcto = True
    else:
        trial != number
        print("Numero incorrecto, sigue intesntando")