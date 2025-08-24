class User:
    def __init__(self, id_usuario, nombre, correo):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo = correo
        self.accesos = []  # Lista de fechas/hora de acceso
    
    