from utils import hash, archive
from utils.config import DATA_FOLDER, USUARIOS_FILE
from models.user import User
from models.access import Access
from datetime import datetime

def main_menu():
    # 1) Inicializa la tabla hash en disco si no existe / está vacía
    #    (tamaño 20 como en tu hash_function)
    hash.initialize_hash_table(20, USUARIOS_FILE, DATA_FOLDER)

    # 2) Crea el manejador de pilas de accesos por dirección
    acceso = Access(size=20, limite=20)

    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Crear usuario")
        print("2. Validar usuario")
        print("3. Almacenar o eliminar acceso")
        print("4. Salir")

        opcion = input("Elige una opción (1-4): ").strip()

        if opcion == "1":
            # Crear usuario
            id_usuario = input("ID del usuario (formato NNCC, p.ej. 12AB): ").strip().upper()
            nombre = input("Nombre: ").strip()
            correo = input("Correo: ").strip()

            usuario = User(id_usuario, nombre, correo)
            # Llama insert_user con los parámetros que espera tu clase
            creado = usuario.insert_user(id_usuario, nombre, correo, acceso=None)
            if creado:
                print(f"Usuario {nombre} creado correctamente.")
            else:
                print("No se pudo crear el usuario.")

        elif opcion == "2":
            # Validar usuario (obtener info)
            id_usuario = input("ID del usuario a validar (NNCC): ").strip().upper()
            usuario = User("", "", "")
            info = usuario.get_user_info(id_usuario)
            if info:
                print("Información del usuario:", info)
            else:
                print("Usuario no encontrado.")

        elif opcion == "3":
            # Almacenar o eliminar acceso
            id_usuario = input("ID del usuario (NNCC): ").strip().upper()
            accion = input("Escribe 'almacenar' para registrar acceso o 'eliminar' para borrar: ").strip().lower()

            # Calcula la dirección entera 0..19
            dir_id = hash.hash_function(id_usuario)
            if dir_id == -1:
                print("ID inválido. Debe cumplir NNCC (2 números + 2 letras).")
                continue

            if accion == "almacenar":
                ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                ok = acceso.push_id(dir_id, ts)
                if ok:
                    # Access.push_id ya persiste el tope en usuarios.txt (campo 'acceso')
                    print(f"Acceso registrado en dirección {dir_id}. Tope actualizado en archivo.")
                else:
                    print("No se pudo registrar el acceso (ID/dirección inválida).")

            elif accion == "eliminar":
                eliminado = acceso.pop_id(dir_id)
                if eliminado is None:
                    print("No hay accesos para eliminar o ID inválido.")
                else:
                    # Access.pop_id también persiste el nuevo tope (o None) en archivo
                    print(f"Eliminado último acceso en dirección {dir_id}: {eliminado}")

            else:
                print("Acción no válida. Usa 'almacenar' o 'eliminar'.")

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
    
    




