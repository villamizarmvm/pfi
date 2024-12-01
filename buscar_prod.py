import sqlite3
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
        print(f"{"Nombre":<20}{"Descripción":<22}{"Cantidad":<10}{"Precio":<10}{"Categoría":<15}")
        print(f"{resultado[0]:<20}{resultado[1]:<22}{resultado[2]:<10}{resultado[3]:<10}{resultado[4]:<15}")
    else:
        print("No se encontró a una persona con ese nombre.")
# Cerrar la conexión
    conexion.close()