    
from typing import Any, Dict, List, Optional
from utils.archive import get_archive_path, read_archive
from utils.config import DATA_FOLDER, USUARIOS_FILE
import json

class Access:
    """
    Maneja pilas de accesos por dirección (ID entero 0..size-1).
    Cada pila guarda timestamps (o lo que le pases) y, al mutar,
    persiste el tope en la tabla hash (usuarios.txt) en esa misma dirección.
    """
    def __init__(self, size: int = 20, limite: int = 20) -> None:
        self.size: int = size
        self.limite: int = limite
        # { id_entero : [acceso1, acceso2, ...] }
        self.pilas: Dict[int, List[Any]] = {i: [] for i in range(size)}

    # -------- utilidades --------
    def existe_pila(self, id_dir: int) -> bool:
        """True si id_dir es entero válido [0, size-1]."""
        return isinstance(id_dir, int) and 0 <= id_dir < self.size

    def _persistir_tope(self, id_dir: int) -> None:
        """
        Escribe el tope actual (o None si vacío) en usuarios.txt,
        en la posición id_dir, en el campo 'acceso'.
        Si la dirección no existe o está None, no hace nada (idempotente).
        """
        if not self.existe_pila(id_dir):
            return

        ruta = get_archive_path(USUARIOS_FILE, DATA_FOLDER)
        tabla = read_archive(ruta)
        if not isinstance(tabla, list):
            return  # archivo vacío/corrupto o no es lista → no persistimos

        if 0 <= id_dir < len(tabla) and tabla[id_dir] is not None:
            tope = self.pilas[id_dir][-1] if self.pilas[id_dir] else None
            # Asegurar que hay dict en esa dirección
            if isinstance(tabla[id_dir], dict):
                tabla[id_dir]["acceso"] = tope
                with open(ruta, "w", encoding="utf-8") as f:
                    json.dump(tabla, f, indent=4)

    # -------- operaciones principales por ID --------
    def push_id(self, id_dir: int, acceso: Any) -> bool:
        """
        Inserta 'acceso' en la pila de id_dir.
        Mantiene tamaño máximo (limite) descartando el más antiguo.
        Persiste el tope en el archivo. Devuelve True si ok.
        """
        if not self.existe_pila(id_dir):
            return False

        pila = self.pilas[id_dir]
        if len(pila) >= self.limite:
            pila.pop(0)  # se va el más viejo
        pila.append(acceso)

        self._persistir_tope(id_dir)
        return True

    def pop_id(self, id_dir: int) -> Optional[Any]:
        """
        Saca y retorna el último acceso (tope) de la pila id_dir.
        Persiste el nuevo tope (o None si quedó vacía).
        Retorna None si id inválido o pila vacía.
        """
        if not self.existe_pila(id_dir):
            return None
        pila = self.pilas[id_dir]
        if not pila:
            return None
        eliminado = pila.pop()
        self._persistir_tope(id_dir)
        return eliminado

    def peek_id(self, id_dir: int) -> Optional[Any]:
        """
        Retorna el tope sin eliminar. None si id inválido o pila vacía.
        """
        if not self.existe_pila(id_dir):
            return None
        pila = self.pilas[id_dir]
        return pila[-1] if pila else None

    def obtener_pila(self, id_dir: int) -> Optional[List[Any]]:
        """
        Retorna una copia de la pila del id_dir. None si id inválido.
        """
        if not self.existe_pila(id_dir):
            return None
        return list(self.pilas[id_dir])

    # -------- “usar verificador y ejecutar” (lo que pidió el encargado) --------
    def verificar_y_push(self, id_dir: int, acceso: Any) -> bool:
        """Usa existe_pila y, si es válida, ejecuta push_id."""
        if not self.existe_pila(id_dir):
            return False
        return self.push_id(id_dir, acceso)

    def verificar_y_pop(self, id_dir: int) -> Optional[Any]:
        """Usa existe_pila y, si es válida, ejecuta pop_id."""
        if not self.existe_pila(id_dir):
            return None
        return self.pop_id(id_dir)


#un metodo que sirva para verificar si existe una pila con el nombre (parametro) y que retorn true o false


#un metodo utilice el metodo de verificar pila y ejecute un pop 

#un metodo utilice el metodo de verificar pila y ejecute un push 

    