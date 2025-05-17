from .conexion_db import ConexionDB
from tkinter import messagebox

# Crear tabla si no existe
def crear_tabla():
    conexion = ConexionDB()
    sql = '''
    CREATE TABLE IF NOT EXISTS peliculas (
        id_pelicula INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(100),
        duracion VARCHAR(10),
        genero VARCHAR(50)
    )
    '''
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        messagebox.showinfo('Crear Registro', 'Se creó la tabla en la BD')
    except:
        messagebox.showwarning('Crear Registro', 'No se pudo crear la tabla (¿ya existe?)')


# Borrar tabla
def borrar_tabla():
    conexion = ConexionDB()
    sql = 'DROP TABLE IF EXISTS peliculas'
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        messagebox.showwarning('Borrar Registro', 'La tabla se borró con éxito')
    except:
        messagebox.showwarning('Borrar Registro', 'No hay tabla para borrar')


# Clase Pelicula
class Pelicula:
    def __init__(self, nombre, duracion, genero):
        self.id_pelicula = None
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero

    def __str__(self):
        return f'Pelicula[{self.nombre}, {self.duracion}, {self.genero}]'


# Guardar una película
def guardar(pelicula):
    conexion = ConexionDB()
    sql = """INSERT INTO peliculas (nombre, duracion, genero) VALUES (?, ?, ?)"""
    valores = (pelicula.nombre, pelicula.duracion, pelicula.genero)
    try:
        conexion.cursor.execute(sql, valores)
        conexion.cerrar()
        messagebox.showinfo('Guardar Película', 'Película guardada correctamente')
    except:
        messagebox.showerror('Guardar Película', 'No se pudo guardar la película. Verifica si la tabla existe.')


def listar():
    conexion=ConexionDB()

    lista_pelicuñas =[]
    sql=' SELECT * FROM peliculas'

    try:
        conexion.cursor.execute(sql)
        lista_peliculas=conexion.cursor.fetchall()
        conexion.cerrar
    except:
        titulo='Conexion al registro'
        mensaje ='Crea la tabla en la base de dato'
        messagebox.showwarning(titulo, mensaje)

    return lista_peliculas

# Listar todas las películas
def listar():
    conexion = ConexionDB()
    lista = []
    sql = 'SELECT * FROM peliculas'
    try:
        conexion.cursor.execute(sql)
        lista = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        messagebox.showerror('Listar Películas', 'No se pudo recuperar la información')
    return lista


# Eliminar una película por ID
def eliminar(id_pelicula):
    conexion = ConexionDB()
    sql = 'DELETE FROM peliculas WHERE id_pelicula = ?'
    try:
        conexion.cursor.execute(sql, (id_pelicula,))
        conexion.cerrar()
        messagebox.showinfo('Eliminar Película', 'Película eliminada correctamente')
    except:
        messagebox.showerror('Eliminar Película', 'No se pudo eliminar la película')

def editar(pelicula, id_pelicula):
    conexion = ConexionDB()

    sql = f"""UPDATE peliculas
              SET nombre = '{pelicula.nombre}', duracion = '{pelicula.duracion}', genero = '{pelicula.genero}'
              WHERE id_pelicula = {id_pelicula}"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Edición de datos'
        mensaje = 'No se ha podido editar este registro'
        messagebox.showerror(titulo, mensaje)


def eliminar(id_pelicula):
    conexion = ConexionDB()

    sql = f'DELETE FROM peliculas WHERE id_pelicula ={id_pelicula}'

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Eliminar datos'
        mensaje = 'No se ha podido eliminar este registro'
        messagebox.showerror(titulo, mensaje)