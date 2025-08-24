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

        


