import sqlite3
def mostrar_productos():
# Conectar a la base de datos
    conexion = sqlite3.connect("inventario_productos.db")
    cursor = conexion.cursor()
# Recuperar todos los registros de la tabla Personas
    cursor.execute("SELECT * FROM Productos")
    resultados = cursor.fetchall()
# Verificar si la tabla tiene registros
    if resultados:
        print("Listado de productos registradas:")
        for registro in resultados:
            print("Nombre:", registro[0], "Descripción:", registro[1],
            "Cantidad:", registro[2], "Precio:", registro[3], "Categoría", registro[4])
    else:
        print("No hay registros en la tabla Personas.")
# Cerrar la conexión
    conexion.close()

