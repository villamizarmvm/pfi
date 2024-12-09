import sqlite3

def registrar_producto():
    
    conexion = sqlite3.connect("./inventario_productos.db")  # Conectar a la base de datos
    cursor = conexion.cursor()
    # Crear la tabla Productos
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT UNIQUE NOT NULL,
        descripcion TEXT NOT NULL,
        cantidad INTEGER NOT NULL,
        precio REAL NOT NULL,
        categoria TEXT NOT NULL
    )
    ''')                                                     

    # Pedir los datos del producto
    nombre = input("Ingrese el nombre del producto: ").capitalize()
    # Verificar si el producto ya existe
    cursor.execute("SELECT * FROM Productos WHERE nombre = ?", (nombre,))
    producto_existente = cursor.fetchone()

    if producto_existente:
        print(f"El producto '{nombre}' ya existe en la base de datos.")
    else:
        descripcion = input("Ingrese la descripcion del producto: ").capitalize()
        categoria = input("Ingrese la categoria del producto: ").capitalize()
        cantidad = 0
        precio = 0.0

        while cantidad <= 0:
            try:
                cantidad = int(input("Ingrese la cantidad en stock: "))
                if cantidad <= 0:
                    print("Ingrese un numero mayor que 0")
            except ValueError:
                print("Ingrese un numero")
                cantidad = 0

        while precio <= 0:
            try:
                precio = float(input("Ingrese el precio del producto: "))
                if precio <= 0:
                    print("Ingrese un numero mayor que 0")
            except ValueError:
                print("Ingrese un numero")
                precio = 0

   
        # Insertar los datos en la tabla Productos
        cursor.execute('''
        INSERT INTO Productos (nombre, descripcion, cantidad, precio, categoria)
        VALUES (?, ?, ?, ?, ?)
        ''', (nombre, descripcion, cantidad, precio, categoria))

        # Confirmar la inserción
        conexion.commit()
        print("Producto registrado con éxito.")

    # Cerrar la conexión
    conexion.close()
    
def buscar_producto():
# Conectar a la base de datos
    conexion = sqlite3.connect("inventario_productos.db")
    cursor = conexion.cursor()
# Pedir el nombre de la persona que se desea buscar
    nombre = input("\nIngrese el nombre del producto que desea buscar: ").capitalize()
# Ejecutar la consulta de búsqueda
    cursor.execute("SELECT * FROM Productos WHERE nombre = ?", (nombre,))
    resultado = cursor.fetchone()
# Verificar si se encontró el registro
    if resultado:
        print("----- Información del producto -----")
        print(f"{"Nombre":<20}{"Descripción":<22}{"Cantidad":<15}{"Precio":<15}{"Categoría":<15}")
        print(f"{resultado[0]:<20}{resultado[1]:<22}{resultado[2]:<15}{resultado[3]:<15}{resultado[4]:<15}")
    else:
        print("No se encontró a una persona con ese nombre.")
# Cerrar la conexión
    conexion.close()
    
def actualizar_cant_prod():
    conexion = sqlite3.connect("inventario_productos.db")
    cursor = conexion.cursor()
    nombre = input("Ingrese el nombre del producto que desea actualizar cantidad: ").capitalize()
    nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
    cursor.execute("UPDATE Productos SET cantidad = ? WHERE nombre = ?",
    (nueva_cantidad, nombre))
    if cursor.rowcount > 0:
        print("La cantidad del producto", nombre, " ha sido actualizada con éxito.")
    else:
        print("No se encontró a un producto con ese nombre.")
    conexion.commit()
    conexion.close()
    
def eliminar_producto():
    conexion = sqlite3.connect("inventario_productos.db")
    cursor = conexion.cursor()
    nombre = input("Ingrese el nombre del producto que desea eliminar:").capitalize()
    cursor.execute("DELETE FROM Productos WHERE nombre = ?", (nombre,))
    if cursor.rowcount > 0:
        print("El producto", nombre, "ha sido eliminado con éxito.")
    else:
        print("No se encontró a un producto con ese nombre.")
    conexion.commit()
    conexion.close()
    
def mostrar_productos():
# Conectar a la base de datos
    conexion = sqlite3.connect("inventario_productos.db")
    cursor = conexion.cursor()
# Recuperar todos los registros de la tabla Personas
    cursor.execute("SELECT * FROM Productos")
    resultados = cursor.fetchall()
# Verificar si la tabla tiene registros
    if resultados:
        print("\n----------------------- Listado de productos registrados -----------------------")
        print(f"\n{"ID":<6}{"Nombre":<20}{"Descripción":<22}{"Cantidad":<12}{"Precio":<12}{"Categoría":<15}")
        for registro in resultados:
            print(f"{registro[0]:<6}{registro[1]:<20}{registro[2]:<22}{registro[3]:<12}{registro[4]:<12}{registro[5]:<15}")
    else:
        print("No hay registros en la tabla Personas.")
# Cerrar la conexión
    conexion.close()

def reporte_bajoStock():
    conexion = sqlite3.connect("inventario_productos.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Productos WHERE cantidad < 100")
    resultados = cursor.fetchall()
    if resultados:
        print("Productos con stock menor a 100 productos :")
        for registro in resultados:
            print("Nombre:", registro[0], "Descripción:", registro[1],
            "Cantidad:", registro[2], "Precio:", registro[3], "Categoría", registro[4])
    else:
        print("No se encontraron productos con menos de 100 productos.")
    conexion.close()

def mostrar_menu():
    while True:
        print("\n--- Menú de Gestión de Inventario ---")
        print("     1. Registrar producto")
        print("     2. Consultar producto")
        print("     3. Actualizar producto")
        print("     4. Eliminar producto")
        print("     5. Listar productos")
        print("     6. Reporte de bajo stock")
        print("     7. Salir")
        opcion = input("\nSeleccione una opción (1-7): ")

        if opcion == '1':
            registrar_producto()
        elif opcion == '2':
            buscar_producto()
        elif opcion == '3':
            actualizar_cant_prod()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            mostrar_productos()
        elif opcion == '6':
            reporte_bajoStock()
        elif opcion == '7':
            print("Saliendo del sistema...")
            break
        else:
            print("\n\nOpción no válida. Intente de nuevo.")
        
mostrar_menu()
        
        