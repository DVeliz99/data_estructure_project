#verificar dirección en el archivo
#insertar valor en la dirección
#obtener información de la dirección
#Verificar si la direccion no esta vacía
import os

#Verifica si un archivo existe en una carpeta dada
def archive_exists(nombre_archivo,carpeta):
    ruta = os.path.join(carpeta,nombre_archivo)
    return os.path.exists(ruta)

#def read_archive(nombre_archivo,carpeta):