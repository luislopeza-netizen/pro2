from tkinter import *
from tkinter import ttk
from sqlite3 import *

# Conexión a la base de datos
base_de_datos = connect("productos.db")
cr = base_de_datos.cursor()

# Crear tabla con columnas ID, Nombre, Precio, Stock
def crearTabla():
    cr.execute('DROP TABLE IF EXISTS productos')  # Elimina si ya existe
    cr.execute('''
        CREATE TABLE productos (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Nombre TEXT NOT NULL,
            Precio TEXT NOT NULL,
            Stock TEXT NOT NULL
        );
    ''')
    base_de_datos.commit()

# Insertar datos de ejemplo
def insertarDatos():
    ejemplo = [
        ("Lapicero", "2.50", "100"),
        ("Cuaderno", "5.00", "50"),
        ("Mochila", "25.00", "20"),
        ("Regla", "1.00", "150")
    ]
    cr.executemany("INSERT INTO productos (Nombre, Precio, Stock) VALUES (?, ?, ?)", ejemplo)
    base_de_datos.commit()

# Obtener datos desde la base
def obtenerDatos():
    cr.execute("SELECT * FROM productos")
    return cr.fetchall()

# Rellenar tabla en la interfaz
def rellenar_tabla():
    for fila in obtenerDatos():
        tabla.insert("", "end", values=fila)

# Crear tabla e insertar datos
crearTabla()
insertarDatos()

# Interfaz gráfica
app = Tk()
app.title("Inventario de Productos")
app.geometry("500x300")

# Crear Treeview
tabla = ttk.Treeview(app, columns=("ID", "Nombre", "Precio", "Stock"), show="headings")
for col in ("ID", "Nombre", "Precio", "Stock"):
    tabla.heading(col, text=col)
    tabla.column(col, anchor="center", width=100)
tabla.pack(pady=20)

# Mostrar datos al iniciar
rellenar_tabla()

# Ejecutar la app
app.mainloop()
