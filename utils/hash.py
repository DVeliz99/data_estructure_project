#funcion de dispersión
#inicializar tabla hash

from . import archive as ar
import json
import os

# Inicializa la tabla hash (crea el archivo desde cero)
def initialize_hash_table(size, nombre_archivo, carpeta):

    # Crear carpeta si no existe
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

    ruta = ar.get_archive_path(nombre_archivo, carpeta)

    if not ar.archive_exists(nombre_archivo, carpeta):
        # Archivo no existe → crear
        return ar.initialize_archive(ruta, size)
    else:
        tabla = ar.read_archive(ruta)
        if tabla is None:
            print("Archivo vacío o corrupto, inicializando tabla hash...")
            return ar.initialize_archive(ruta, size)
        print("El archivo ya existe, cargando tabla hash...")
        return tabla
    
#ids con formato NNCC (2 números + 2 letras). 
def hash_function(id_usuario: str) -> int:
    
    try:
        if len(id_usuario) != 4 or not id_usuario[:2].isdigit() or not id_usuario[2:].isalpha():
            raise ValueError("El id debe tener el formato NNCC (2 números + 2 letras).")
    
        # Convertimos los dos primeros caracteres a un número
        numeros = int(id_usuario[:2])
    
        # Convierte letras a números usando sus códigos ASCII y suma sus valores correspondientes
        letras = sum(ord(c) for c in id_usuario[2:])
    
        # Combinamos ambas partes
        valor = numeros * 100 + letras
    
        return valor % 20
    except Exception as e:
        print(f"Error en la función hash: {e}")
        return -1







