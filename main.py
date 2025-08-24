from utils import hash

if __name__ == "__main__":
    # Parámetros de prueba
    size = 20
    nombre_archivo = "usuarios.txt"
    carpeta = "data"

    # Inicializar la tabla hash en el archivo
    hash.initialize_hash_table(size, nombre_archivo, carpeta)
