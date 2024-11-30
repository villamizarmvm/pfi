import sqlite3
def buscar_producto():
# Conectar a la base de datos
    conexion = sqlite3.connect("base_datos.db")
    cursor = conexion.cursor()
# Pedir el nombre de la persona que se desea buscar
    nombre = input("Ingrese el nombre del producto que desea buscar: ")
# Ejecutar la consulta de búsqueda
    cursor.execute("SELECT * FROM Producto WHERE nombre = ?", (nombre,))
    resultado = cursor.fetchone()
# Verificar si se encontró el registro
    if resultado:
        print("Información de la persona encontrada:")
        print("Nombre:", resultado[0])
        print("Descripción:", resultado[1])
        print("Cantidad:", resultado[2])
        print("Precio:", resultado[3])
        print("Categoría", resultado[4])
    else:
        print("No se encontró a una persona con ese nombre.")
# Cerrar la conexión
    conexion.close(