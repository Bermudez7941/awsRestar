cantidad=input("ingrese la cantidad a imprimir: ")
myVariable=input("Ingrese cualquier valor: ")

i = 0
while i < int(cantidad):
    print("{} is of the data type {}".format(myVariable,type(myVariable)))
    myVariable=input("Ingrese cualquier valor: ")
    i = i + 1  
    

