import sqlite3
def registrar_producto():
    # Conectar a la base de datos
    conexion = sqlite3.connect("inventario_productos.db")
    cursor = conexion.cursor()

    # Crear la tabla Personas
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Productos (
    nombre TEXT,
    descripcion TEXT,
    cantidad INTEGER,
    precio REAL,
    categoria TEXT
    )
    ''')
    # Pedir los datos de la persona
    nombre = input("Ingrese el nombre del producto: ").capitalize()
    descripcion = input("Ingrese la descripcion del producto: ").capitalize()
    categoria = input("Ingrese la categoria del producto: ").capitalize()
    cantidad = 0
    precio = 0.0
    while cantidad <= 0:
        try:
            cantidad = int(input("Ingrese la cantidad en stock: "))
            if cantidad <=0:
                print("Ingrese un numero mayor que 0")
        except ValueError:
            print("Ingrese un numero")
            cantidad = 0
    while precio <=0:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            if precio <=0:
                print("Ingrese un numero mayor que 0")
        except ValueError:
            print("Ingrese un numero")
            precio = 0
    # Insertar los datos en la tabla Personas
    cursor.execute('''
    INSERT INTO Productos (nombre, descripcion, cantidad, precio, categoria)
    VALUES (?, ?, ?, ?, ?)
    ''', (nombre, descripcion, cantidad, precio, categoria))
    # Confirmar la inserción
    conexion.commit()
    print("Producto registrada con éxito.")
    # Cerrar la conexión
    conexion.close()