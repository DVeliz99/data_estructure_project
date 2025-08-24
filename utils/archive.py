#verificar dirección en el archivo
#insertar valor en la dirección
#obtener información de la dirección
#Verificar si la direccion no esta vacía
import os
import json

#Obtiene la ruta completa del archivo en la carpeta dada
def get_archive_path(nombre_archivo,carpeta):
    return os.path.join(carpeta,nombre_archivo)

#Verifica si un archivo existe en una carpeta dada
def archive_exists(nombre_archivo,carpeta):
    return os.path.exists(get_archive_path(nombre_archivo, carpeta))

#Inicializa el archivo con una tabla hash vacía de tamaño dado
def initialize_archive(ruta, size):
    tabla_hash = [None] * size
    with open(ruta, "w") as archivo:
        json.dump(tabla_hash, archivo, indent=4) #aplica sangría de 4 espacios para mejor legibilidad
    print(f"Tabla hash inicializada con {len(tabla_hash)} posiciones")
    return tabla_hash


# Leer la tabla hash desde el archivo
def read_archive(ruta):
    if os.path.exists(ruta):
        # Si el archivo está vacío, inicializar lista vacía
        if os.path.getsize(ruta) == 0:
            print("Archivo vacío, devolviendo None.")
            return None
        try:
            with open(ruta, "r") as archivo:
                return json.load(archivo)
        except json.JSONDecodeError:
            print("Archivo corrupto o sin formato JSON válido, devolviendo None.")
            return None
    else:
        print("No se puede leer: el archivo no existe.")
        return None

def address_exists(nombre_archivo,carpeta, direccion):
    ruta= get_archive_path(nombre_archivo, carpeta)
    
    if not archive_exists(nombre_archivo, carpeta):
        raise FileNotFoundError(f"El archivo {nombre_archivo} no existe en la carpeta {carpeta}")
    
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            tabla_hash = json.load(archivo)  # convierte JSON a lista de Python

        # Solo se verifica si la dirección existe en la tabla
        if 0 <= direccion < len(tabla_hash):
            return direccion
        return -1
    
    except Exception as e:
        print(f"Se produjo un error al leer el archivo: {e}")
        return -1

def is_address_empty(nombre_archivo, carpeta, direccion):
    try:
        if address_exists(nombre_archivo, carpeta, direccion) == -1:
            return None  # dirección fuera de rango

        ruta = get_archive_path(nombre_archivo, carpeta)
        with open(ruta, 'r', encoding='utf-8') as archivo:
            tabla_hash = json.load(archivo)

        return tabla_hash[direccion] is None

    except (FileNotFoundError, json.JSONDecodeError, IndexError):
        return None
        

