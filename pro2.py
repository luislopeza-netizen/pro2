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

def insertarDatos():
    ejemplo = [
        ("Lapicero", "2.50", "100"),
        ("Cuaderno", "5.00", "50"),
        ("Mochila", "25.00", "20"),
        ("Regla", "1.00", "150")
    ]
    for producto in ejemplo:
        cr.execute("INSERT INTO productos (Nombre, Precio, Stock) VALUES (?, ?, ?)", producto)
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
app.geometry("500x500")

# Crear Treeview
tabla = ttk.Treeview(app, columns=("ID", "Nombre", "Precio", "Stock"), show="headings")
for col in ("ID", "Nombre", "Precio", "Stock"):
    tabla.heading(col, text=col)
    tabla.column(col, anchor="center", width=100)
tabla.pack(pady=20)

def abrir_formulario_agregar():
    ventana_agregar = Toplevel(app)
    ventana_agregar.title("Agregar Producto")
    ventana_agregar.geometry("300x200")

    Label(ventana_agregar, text="Nombre").grid(row=0, column=0, padx=10, pady=5)
    entry_nombre = Entry(ventana_agregar)
    entry_nombre.grid(row=0, column=1, padx=10, pady=5)

    Label(ventana_agregar, text="Precio").grid(row=1, column=0, padx=10, pady=5)
    entry_precio = Entry(ventana_agregar)
    entry_precio.grid(row=1, column=1, padx=10, pady=5)

    Label(ventana_agregar, text="Stock").grid(row=2, column=0, padx=10, pady=5)
    entry_stock = Entry(ventana_agregar)
    entry_stock.grid(row=2, column=1, padx=10, pady=5)

    def agregar_desde_ventana():
        nombre = entry_nombre.get()
        precio = entry_precio.get()
        stock = entry_stock.get()
        if nombre and precio and stock:
            cr.execute("INSERT INTO productos (Nombre, Precio, Stock) VALUES (?, ?, ?)", (nombre, precio, stock))
            base_de_datos.commit()
            tabla.insert("", "end", values=(cr.lastrowid, nombre, precio, stock))
            ventana_agregar.destroy()

    Button(ventana_agregar, text="Agregar", command=agregar_desde_ventana).grid(row=3, column=0, columnspan=2, pady=10)

# Botón en la ventana principal para abrir el formulario
boton_agregar = Button(app, text="Agregar Producto", command=abrir_formulario_agregar)
boton_agregar.pack(pady=10)

def abrir_formulario_eliminar():
    ventana_eliminar = Toplevel(app)
    ventana_eliminar.title("Eliminar Producto")
    ventana_eliminar.geometry("300x150")

    Label(ventana_eliminar, text="ID del producto a eliminar").pack(pady=10)
    entry_id = Entry(ventana_eliminar)
    entry_id.pack(pady=5)

    def eliminar_producto():
        id_producto = entry_id.get()
        if id_producto.isdigit():
            cr.execute("DELETE FROM productos WHERE ID = ?", (id_producto,))
            base_de_datos.commit()

            # Limpiar y actualizar tabla
            for item in tabla.get_children():
                tabla.delete(item)
            rellenar_tabla()

            ventana_eliminar.destroy()

    Button(ventana_eliminar, text="Eliminar", command=eliminar_producto).pack(pady=10)

boton_eliminar = Button(app, text="Eliminar Producto", command=abrir_formulario_eliminar)
boton_eliminar.pack(pady=5)

# Mostrar datos al iniciar
rellenar_tabla()

# Ejecutar la app
app.mainloop()
