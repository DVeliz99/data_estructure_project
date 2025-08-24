#indica que la carpeta es un paquete
from .user import User
from .access import Access


# __all__ define lo que se importa con from models import *
__all__ = ["User", "Access"]