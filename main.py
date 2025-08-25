from utils import hash, archive
from models.user import User

def main_menu():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Crear usuario")
        print("2. Validar usuario")
        print("3. Almacenar o eliminar acceso")
        print("4. Salir")

        opcion = input("Elige una opción (1-4): ").strip()

        if opcion == "1":
            # Crear usuario
            id_usuario = input("ID del usuario: ").strip()
            nombre = input("Nombre: ").strip()
            correo = input("Correo: ").strip()
            usuario = User(id_usuario, nombre, correo)
            if usuario.insert_user():
                print(f"Usuario {nombre} creado correctamente.")
            else:
                print("No se pudo crear el usuario.")

        elif opcion == "2":
            # Validar usuario (obtener info)
            id_usuario = input("ID del usuario a validar: ").strip()
            usuario = User("", "", "")
            info = usuario.get_user_info(id_usuario)
            if info:
                print("Información del usuario:", info)
            else:
                print("Usuario no encontrado.")

        elif opcion == "3":
            # Almacenar o eliminar acceso
            id_usuario = input("ID del usuario: ").strip()
            accion = input("Escribe 'almacenar' para registrar acceso o 'eliminar' para borrar: ").strip().lower()
            

        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main_menu()
    # Parámetros de prueba
    # size = 20
    # nombre_archivo = "usuarios.txt"
    # carpeta = "data"
    
    #usuario1 = User(
    #id_usuario="12AB",
    #nombre="Dario Veliz",
    #correo="dario@example.com",
    #acceso="2025-08-24 16:00"
    #)

    # Inicializar la tabla hash en el archivo
    #hash.initialize_hash_table(size, nombre_archivo, carpeta)
    #print(archive.is_address_empty(nombre_archivo, carpeta, hash.hash_function("80ZZ"))) 
    # Insertar el usuario en la tabla hash
    #usuario1.insert_user(usuario1.id_usuario, usuario1.nombre, usuario1.correo, usuario1.acceso)
    

    

    # usuario = User("12AB", "", "","")
    # info = usuario.get_user_info("12AB")

    # if info:
    #     print("Información del usuario:", info)
    # else:
    #     print("Usuario no encontrado o error.")
    
    




