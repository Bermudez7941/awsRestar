import json

# Ejemplo de datos en formato JSON
json_data = '''
{
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "México"
}
'''

# Convertir el JSON a un objeto Python (diccionario)
datos = json.loads(json_data)

# Acceder a los valores del objeto Python
nombre = datos["nombre"]
edad = datos["edad"]
ciudad = datos["ciudad"]

# Imprimir los valores
print("Nombre:", nombre)
print("Edad:", edad)
print("Ciudad:", ciudad)

# Convertir un objeto Python a JSON
datos["profesion"] = "Ingeniero"
json_data_nuevo = json.dumps(datos)

# Imprimir el JSON resultante
print("JSON resultante:")
print(json_data_nuevo)