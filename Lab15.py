import subprocess
nombre_archivo = input("Ingrese el nombre del archivo a filtrar: ")

comando = f"ls | grep {nombre_archivo}"

resultado = subprocess.run(comando, capture_output=True, text=True, shell=True)


if resultado.returncode == 0:
    print(resultado.stdout)
else:
    print(resultado.stderr)