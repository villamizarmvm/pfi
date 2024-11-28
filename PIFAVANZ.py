class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

class Inventario:
    def __init__(self):
        self.productos = []

    def registrar_producto(self):
        
        precio = float(input("Precio por unidad: "))
        nuevo_producto = Producto(nombre, cantidad, precio)
        self.productos.append(nuevo_producto)
        print(f"Producto '{nombre}' registrado con éxito.")

    def consultar_producto(self):
        nombre = input("Nombre del producto a consultar: ")
        for producto in self.productos:
            if producto.nombre == nombre:
                print(f"Nombre: {producto.nombre}, Cantidad: {producto.cantidad}, Precio: {producto.precio}")
                return
        print("Producto no encontrado.")

    def actualizar_producto(self):
        nombre = input("Nombre del producto a actualizar: ")
        for producto in self.productos:
            if producto.nombre == nombre:
                cantidad = int(input("Nueva cantidad disponible: "))
                producto.cantidad = cantidad
                print(f"Producto '{nombre}' actualizado con éxito.")
                return
        print("Producto no encontrado.")

    def eliminar_producto(self):
        nombre = input("Nombre del producto a eliminar: ")
        for producto in self.productos:
            if producto.nombre == nombre:
                self.productos.remove(producto)
                print(f"Producto '{nombre}' eliminado con éxito.")
                return
        print("Producto no encontrado.")

    def listar_productos(self):
        if not self.productos:
            print("No hay productos en el inventario.")
            return
        for producto in self.productos:
            print(f"Nombre: {producto.nombre}, Cantidad: {producto.cantidad}, Precio: {producto.precio}")

    def reporte_bajo_stock(self):
        bajo_stock = [producto for producto in self.productos if producto.cantidad < 5]
        if not bajo_stock:
            print("No hay productos con bajo stock.")
            return
        for producto in bajo_stock:
            print(f"Nombre: {producto.nombre}, Cantidad: {producto.cantidad}, Precio: {producto.precio}")

def menu():
    inventario = Inventario()
    while True:
        print("\n--- Menú de Gestión de Inventario ---")
        print("1. Registrar producto")
        print("2. Consultar producto")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Listar productos")
        print("6. Reporte de bajo stock")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            inventario.registrar_producto()
        elif opcion == '2':
            inventario.consultar_producto()
        elif opcion == '3':
            inventario.actualizar_producto()
        elif opcion == '4':
            inventario.eliminar_producto()
        elif opcion == '5':
            inventario.listar_productos()
        elif opcion == '6':
            inventario.reporte_bajo_stock()
        elif opcion == '7':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()