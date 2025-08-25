from utils import hash, archive
from utils.config import DATA_FOLDER, USUARIOS_FILE
import os
import json

class User:
    def __init__(self, id_usuario, nombre, correo,acceso):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo = correo
        self.acceso=acceso 
        
    def insert_user(self, id_usuario, nombre, correo, acceso):
    
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo = correo
        self.acceso = acceso

        hash_address = hash.hash_function(self.id_usuario)

        try:
            # Verificar si la dirección está vacía
            if archive.is_address_empty(USUARIOS_FILE, DATA_FOLDER, hash_address):
                ruta = archive.get_archive_path(USUARIOS_FILE, DATA_FOLDER)
            
                # Leer la tabla hash
                tabla_hash = archive.read_archive(ruta)

                # Insertar el usuario en la posición del hash
                tabla_hash[hash_address] = {
                "id_usuario": self.id_usuario,
                "nombre": self.nombre,
                "correo": self.correo,
                "acceso": self.acceso
                }

                # Sobrescribir el archivo con la tabla actualizada
                with open(ruta, 'w', encoding='utf-8') as archivo:
                    json.dump(tabla_hash, archivo, indent=4)
                print(f"La información ha sido añadida a la dirección {hash_address}.")

                return True  # Inserción exitosa

            else:
                print(f"La dirección {hash_address} ya está ocupada.")
                return False

        except Exception as e:
            print(f"Error al insertar usuario: {e}")
        return False

            
            
        
        
        
        
        
