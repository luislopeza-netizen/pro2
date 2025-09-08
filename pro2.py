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

# creacion de ventanas 
ventana = Tk()
ventana.title("Lista de Estudiantes")
ventana.geometry("500x300")

# Crear Treeview
tabla = ttk.Treeview(ventana, columns=("ID", "Nombre", "Marca", "Stock"), show="headings")
tabla.heading("ID", text="ID")
tabla.heading("Nombre", text="Nombre")
tabla.heading("Marca", text="Marca")
tabla.heading("Stock", text="Stock")


