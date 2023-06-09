import re

# Abrir el archivo de entrada
with open('preproinsulin-seq.txt', 'r') as archivo_entrada:
    contenido = archivo_entrada.readlines()

# Eliminar las líneas no deseadas usando expresiones regulares, eliminar espacios y saltos de línea
contenido_limpio = [re.sub(r"(ORIGIN|1|61|//|\s+)", "", linea).strip() for linea in contenido]

# Eliminar las filas vacías
contenido_limpio = list(filter(None, contenido_limpio))

# Crear el nuevo archivo con el contenido limpio en una sola línea
contenido_final = ''.join(contenido_limpio)

# Crear el nuevo archivo con el contenido limpio en una sola línea
with open('preproinsulin-seq-clean.txt', 'w') as archivo_salida:
    archivo_salida.write(contenido_final)

# Leer el archivo lsinsulin-seq-clean.txt
with open('preproinsulin-seq-clean.txt', 'r') as archivo_entrada:
    contenido = archivo_entrada.read()

# Obtener las porciones específicas del contenido
lsinsulin = contenido[0:24]
binsulin = contenido[24:54]
cinsulin = contenido[54:89]
ainsulin = contenido[89:111]
insulin = binsulin + ainsulin

print(f"The sequence of human preproinsulin: ", contenido)

# Printing to console using concatenated strings inside the print function (one-liner):
print("The sequence of human insulin, chain a: " + ainsulin)


aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
'V': 117.15, 'W': 204.23, 'Y': 181.19}  

# Count the number of each amino acids  
aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A', 'C','D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T','V', 'W', 'Y']}) 

# Multiply the count by the weights  
molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T', 'V', 'W', 'Y']}.values())  
print("The rough molecular weight of insulin: " +
str(molecularWeightInsulin))

molecularWeightInsulinActual = 5807.63
print("Error percentage: " + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))

