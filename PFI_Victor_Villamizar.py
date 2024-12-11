import sqlite3

def registrar_producto():
    
    conexion = sqlite3.connect("./inventario_productos.db")  # Conectamos a la base de datos
    cursor = conexion.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT UNIQUE NOT NULL,
        descripcion TEXT,
        cantidad INTEGER NOT NULL,
        precio REAL NOT NULL,
        categoria TEXT
    )
    ''')                                       # Si al tabla no existe la crea con el nombre Productos                                               

    nombre = input("Ingrese el nombre del producto: ").capitalize()       # Pedimos el nombre del producto y garantizamos que el nombre guardado comience con mayúscula
    cursor.execute("SELECT * FROM Productos WHERE nombre = ?", (nombre,)) # Verificamos si el nombre del producto ya existe
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
                cantidad = int(input("Ingrese la cantidad en stock: "))   # Garantizamos que la catidad en stock sea un entero positivo
                if cantidad <= 0:
                    print("Ingrese un numero mayor que 0")
            except ValueError:
                print("Ingrese un numero")
                cantidad = 0
        while precio <= 0:
            try:
                precio = float(input("Ingrese el precio del producto: "))  # Garantizamos que el precio del producto sea un real positivo
                if precio <= 0:
                    print("Ingrese un numero mayor que 0")
            except ValueError:
                print("Ingrese un numero")
                precio = 0 
        cursor.execute('''
        INSERT INTO Productos (nombre, descripcion, cantidad, precio, categoria)
        VALUES (?, ?, ?, ?, ?)
        ''', (nombre, descripcion, cantidad, precio, categoria)) # Insertamos los datos en la tabla Productos
       
        conexion.commit()                          # Guardamos cambios realizados en la base de datos
        print("Producto registrado con éxito.")    # Confirmamos la inserción
        
    conexion.close()                               # Cerramos la conexión
    
def buscar_producto():

    conexion = sqlite3.connect("inventario_productos.db")  # Conectamos a la base de datos
    cursor = conexion.cursor()
    nombre = input("\nIngrese el nombre del producto que desea buscar: ").capitalize() # Pedir el nombre del producto que se desea buscar
    cursor.execute("SELECT * FROM Productos WHERE nombre = ?", (nombre,))              # Ejecutamos la consulta de búsqueda
    resultado = cursor.fetchone()
                                                                          
    if resultado:                                                         # Verificamos si se encontró el registro
        print("\n------------------------------ Información del producto ------------------------------")
        print(f"{"ID":<6}{"Nombre":<20}{"Descripción":<22}{"Cantidad":<15}{"Precio":<15}{"Categoría":<15}")
        print(f"{resultado[0]:<6}{resultado[1]:<20}{resultado[2]:<22}{resultado[3]:<15}{resultado[4]:<15}{resultado[5]:<15}")
    else:
        print("No se encontró a una persona con ese nombre.")

    conexion.close()                                # Cerramos la conexión
    
def actualizar_cant_prod():
    conexion = sqlite3.connect("inventario_productos.db")
    cursor = conexion.cursor()
    nombre = input("Ingrese el nombre del producto que desea actualizar cantidad: ").capitalize()
    nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
    cursor.execute("UPDATE Productos SET cantidad = ? WHERE nombre = ?", # Aqui actualizamos la cantidad del producto
    (nueva_cantidad, nombre))
    if cursor.rowcount > 0:                                              # rowcount detecta el número de filas afectadas por la ultima operación
        print("La cantidad del producto", nombre, " ha sido actualizada con éxito.")
    else:
        print("No se encontró a un producto con ese nombre.")
    conexion.commit()                               # Guardamos cambios realizados
    conexion.close()                                # Cerramos la conexión
    
def eliminar_producto():
    conexion = sqlite3.connect("inventario_productos.db")
    cursor = conexion.cursor()
    nombre = input("Ingrese el nombre del producto que desea eliminar:").capitalize()
    cursor.execute("DELETE FROM Productos WHERE nombre = ?", (nombre,))   # Aqui eliminamos el producto
    if cursor.rowcount > 0:
        print("El producto", nombre, "ha sido eliminado con éxito.")
    else:
        print("No se encontró a un producto con ese nombre.")
    conexion.commit()                                # Guardamos cambios realizados
    conexion.close()                                 # Cerramos la conexión
    
def mostrar_productos():

    conexion = sqlite3.connect("inventario_productos.db") # Conectamos a la base de datos
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Productos") # Recuperamos todos los registros de la tabla Productos 
    resultados = cursor.fetchall()

    if resultados:    # Verificamos si la tabla tiene registros
        print("\n----------------------- Listado de productos registrados -----------------------")
        print(f"\n{"ID":<6}{"Nombre":<20}{"Descripción":<22}{"Cantidad":<12}{"Precio":<12}{"Categoría":<15}")
        for registro in resultados:
            print(f"{registro[0]:<6}{registro[1]:<20}{registro[2]:<22}{registro[3]:<12}{registro[4]:<12}{registro[5]:<15}")
    else:
        print("No hay registros en la tabla Personas.")

    conexion.close()  # Cerramos la conexión

def reporte_bajoStock():
    conexion = sqlite3.connect("inventario_productos.db")
    cursor = conexion.cursor()
    limite = 0
    while limite <= 0:
            try:
                limite = int(input("\nIntroduzca el limite de bajo stock: "))   # Garantizamos que el limite de bajo stock sea un entero positivo
                if limite <= 0:
                    print("Ingrese un numero mayor que 0")
            except ValueError:
                print("Ingrese un numero")
                limite = 0

    cursor.execute("SELECT * FROM Productos WHERE cantidad < ?",(limite,))
    resultados = cursor.fetchall()
    if resultados:
        print(F"\n------------- Productos con stock menor a {limite} productos -------------")
        print(f"\n{"ID":<6}{"Nombre":<20}{"Descripción":<22}{"Cantidad":<12}{"Precio":<12}{"Categoría":<15}")
        for registro in resultados:
            print(f"{registro[0]:<6}{registro[1]:<20}{registro[2]:<22}{registro[3]:<12}{registro[4]:<12}{registro[5]:<15}")
    else:
        print(f"\nNo se encontraron productos con stock menor a {limite} productos.")
    conexion.close()

def mostrar_menu():                          # menú principal
    while True:
        print("\n--- Menú de Gestión de Inventario ---")
        print("     1. Agregar producto")
        print("     2. Mostrar producto")
        print("     3. Actualizar cantidad de producto")
        print("     4. Eliminar producto")
        print("     5. Buscar productos")
        print("     6. Reporte de bajo stock")
        print("     7. Salir")
        opcion = input("\nSeleccione una opción (1-7): ")

        if opcion == '1':                   # llamado de funciones según la opción seleccionada
            registrar_producto()
        elif opcion == '2':
            mostrar_productos()
        elif opcion == '3':
            actualizar_cant_prod()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            buscar_producto()
        elif opcion == '6':
            reporte_bajoStock()
        elif opcion == '7':
            print("Saliendo del sistema...")
            break
        else:
            print("\n\nOpción no válida. Intente de nuevo.")
        
mostrar_menu()
        
        