import sqlite3
import os

class ConexionDB:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))  # Ruta absoluta a /model
        db_folder = os.path.join(base_dir, "../database")
        os.makedirs(db_folder, exist_ok=True)  # Asegura que exista la carpeta

        self.base_datos = os.path.join(db_folder, "peliculas.db")  # Ruta completa a la BD
        self.conexion = sqlite3.connect(self.base_datos)
        self.cursor = self.conexion.cursor()

    def cerrar(self):
        self.conexion.commit()
        self.conexion.close()
