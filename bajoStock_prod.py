import sqlite3
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