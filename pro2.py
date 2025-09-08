from tkinter import *
from tkinter import ttk
from sqlite3 import *

# CREAMOS BASE DE DATOS 
base_de_datos = connect("pro2.db")
cr = base_de_datos.cursor()

def crearTabla():
    cr.execute('''
        CREATE TABLE IF NOT EXISTS estudiantes(
        ID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        Nombre TEXT NOT NULL,
        Marca TEXT NOT NULL,
        Stock TEXT NOT NULL);
        ''')
    base_de_datos.commit()
    print("Tabla creada")

crearTabla()

cr.execute('SELECT * FROM estudiantes')
datos = cr.fetchall()

