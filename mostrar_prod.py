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
        print(f"{"Nombre":<20}{"Descripción":<22}{"Cantidad":<10}{"Precio":<10}{"Categoría":<15}")
        for registro in resultados:
            print(f"{registro[0]:<20}{registro[1]:<22}{registro[2]:<10}{registro[3]:<10}{registro[4]:<15}")
    else:
        print("No hay registros en la tabla Personas.")
# Cerrar la conexión
    conexion.close()

