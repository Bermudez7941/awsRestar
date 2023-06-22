print("aca esta mi archivo:\n")
f1=open("files/diario.txt","r")
print(f1.read())
f1.close()

print("aca esta mi otro archivo llamado nuevo archivo:\n")
f2=open("files/nuevoarchivo.txt","w")
f2.write("Este es la priemera linea")
f2.close()

print("aca esta mi otro archivo llamado nuevo archivo:\n")
f3=open("files/nuevoarchivo.txt","a")
f3.write("Este es otra linea")
f3.close()