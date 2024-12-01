import sqlite3
import registro_prod, mostrar_prod, buscar_prod, bajoStock_prod

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
            registro_prod.registrar_producto()
        elif opcion == '2':
            buscar_prod.buscar_producto()
        elif opcion == '3':
            actualizar_cant_prod()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            mostrar_prod.mostrar_productos()
        elif opcion == '6':
            bajoStock_prod.reporte_bajoStock()
        elif opcion == '7':
            print("Saliendo del sistema...")
            break
        else:
            print("\n\nOpción no válida. Intente de nuevo.")
        
mostrar_menu()
        
        