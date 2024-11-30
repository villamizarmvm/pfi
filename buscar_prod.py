import sqlite3
def buscar_producto():
# Conectar a la base de datos
    conexion = sqlite3.connect("inventario_productos.db")
    cursor = conexion.cursor()
# Pedir el nombre de la persona que se desea buscar
    nombre = input("Ingrese el nombre del producto que desea buscar: ").capitalize()
# Ejecutar la consulta de búsqueda
    cursor.execute("SELECT * FROM Productos WHERE nombre = ?", (nombre,))
    resultado = cursor.fetchone()
# Verificar si se encontró el registro
    if resultado:
        print("-----Información del producto-----")
        print("Nombre:", resultado[0])
        print("Descripción:", resultado[1])
        print("Cantidad:", resultado[2])
        print("Precio:", resultado[3])
        print("Categoría:", resultado[4])
    else:
        print("No se encontró a una persona con ese nombre.")
# Cerrar la conexión
    conexion.close()