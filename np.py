import numpy as np

# Crear un arreglo unidimensional
arr = np.array([1, 2, 3, 4, 5])
print("Arreglo unidimensional:")
print(arr)

# Crear un arreglo bidimensional
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print("Arreglo bidimensional:")
print(arr2d)

# Acceder a elementos del arreglo
print("Primer elemento del arreglo unidimensional:", arr[0])
print("Elemento en la segunda fila y segunda columna del arreglo bidimensional:", arr2d[1, 1])

# Operaciones matemáticas con arreglos
print("Suma de elementos del arreglo unidimensional:", np.sum(arr))
print("Promedio de elementos del arreglo bidimensional:", np.mean(arr2d))

# Operaciones de manipulación de arreglos
arr3 = np.arange(1, 6)  # Crear un arreglo con valores del 1 al 5
print("Arreglo generado con np.arange:", arr3)

arr4 = np.linspace(1, 10, 5)  # Crear un arreglo con 5 elementos espaciados linealmente de 1 a 10
print("Arreglo generado con np.linspace:", arr4)

# Operaciones de álgebra lineal
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
c = np.dot(a, b)  # Producto de matrices
print("Producto de matrices:")
print(c)