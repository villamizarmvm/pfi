inventario = {
1: {"nombre": "Manzana", "descripcion": "Fruta fresca",
        "cantidad": 3, "precio": 0.5, "categoria": "Frutas"
    },
2: {"nombre": "Pan", "descripcion": "Pan casero",
        "cantidad": 20, "precio": 1.0, "categoria": "Panadería"
    }
}

contador_codigo = 2

def registro_productos(contador):
    contador_codigo = contador + 1
    nombre = input("Ingrese el nombre del producto: ").capitalize()
    descripcion = input("Ingrese la descripcion del producto: ").capitalize()
    categoria = input("Ingrese la categoria del producto: ").capitalize()
    cantidad = 0
    precio = 0.0
    while cantidad <= 0:
        try:
            cantidad = int(input("Ingrese la cantidad en stock: "))
            if cantidad <=0:
                print("Ingrese un numero mayor que 0")
        except ValueError:
            print("Ingrese un numero")
            cantidad = 0
    while precio <=0:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            if precio <=0:
                print("Ingrese un numero mayor que 0")
        except ValueError:
            print("Ingrese un numero")
            precio = 0
    inventario[contador_codigo] = {"nombre": nombre, "descripcion": descripcion, "cantidad": cantidad,"precio": precio,"categoria": categoria}
    print("Producto agregado exitosamente")

def mostrar_productos(productos_a_mostrar = inventario):
    if len(productos_a_mostrar) == 0:
        print("El inventario esta vacio")
    else:
        print(f"{"Codigo":<10}{"Nombre":<20}{"descripcion":<20}{"cantidad":<10}{"precio":<10}{"categoria":<10}")
        for codigo, producto in productos_a_mostrar.items():
            print(f"{codigo:<10}{producto["nombre"]:<20}{producto["descripcion"]:<20}{producto["cantidad"]:<10}{producto["precio"]:<10}{producto["categoria"]:<10}")

def actualizar_producto():
    print("Los productos en el inventario son: ")
    mostrar_productos()
    codigo = 0
    while codigo <= 0:
        try:
            codigo = int(input("Ingrese el codigo del producto a modificar/actualizar: "))
            if codigo <=0:
                print("Ingrese un numero mayor que 0")
        except ValueError:
            print("Ingrese un numero")
            codigo = 0
    resultado = inventario.get(codigo, "No encontrado")
    if resultado == "No encontrado":
        print("Codigo incorrecto, ningun producto con ese codigo")
    else:
        print(f"{codigo:<10}{resultado["nombre"]:<20}{resultado["descripcion"]:<20}{resultado["cantidad"]:<10}{resultado["precio"]:<10}{resultado["categoria"]:<10}")
        nombre = input("Ingrese el nuevo nombre del producto: ").capitalize()
        descripcion = input("Ingrese la nueva descripcion del producto: ").capitalize()
        categoria = input("Ingrese la nueva categoria del producto: ").capitalize()
        cantidad = 0
        precio = 0.0
        while cantidad <= 0:
            try:
                cantidad = int(input("Ingrese la cantidad en stock: "))
                if cantidad <=0:
                    print("Ingrese un numero mayor que 0")
            except ValueError:
                print("Ingrese un numero")
                cantidad = 0
        while precio <=0:
            try:
                precio = float(input("Ingrese el precio del producto: "))
                if precio <=0:
                    print("Ingrese un numero mayor que 0")
            except ValueError:
                print("Ingrese un numero")
                precio = 0
        inventario[codigo] = {"nombre": nombre, "descripcion": descripcion, "cantidad": cantidad,"precio": precio,"categoria": categoria}
        print("Producto actualizado exitosamente")

def listar_stock_bajo(inventario):
    try:
        valor_ingresado = int(input("Ingrese el valor minimo de unidades: "))
        productos_filtrados = {
            cod_producto: detalles
            for cod_producto, detalles in inventario.items()
            if detalles['cantidad'] <= valor_ingresado
        }
        print("\nProductos que cumplen con la condición (cantidad <= {}):".format(valor_ingresado))
        if productos_filtrados:
            for cod_producto, detalles in productos_filtrados.items():
                print(f"Código: {cod_producto}, Nombre: {detalles['nombre']}, "
                      f"Descripción: {detalles['descripcion']}, Cantidad: {detalles['cantidad']}, "
                      f"Precio: {detalles['precio']}")
        else:
            print("No se encontraron productos que cumplan la condición.")
    except ValueError:
        print("Error: Por favor, ingrese un número válido.")

def reporte_bajo_stock():
    cantidad = 0
    while cantidad <= 0:
            try:
                cantidad = int(input("Ingrese la cantidad minima que puede haber: "))
                if cantidad <=0:
                    print("Ingrese un numero mayor que 0")
            except ValueError:
                print("Ingrese un numero")
                cantidad = 0
    productos_bajo_stock = {}
    for codigo, producto in inventario.items():
        if producto["cantidad"] <= cantidad:
            productos_bajo_stock[codigo] = producto
    if len(productos_bajo_stock) == 0:
        print("No hay productos con bajo stock")
    else:
        print("Los procdutos con bajo stock son: ")
        mostrar_productos(productos_bajo_stock)

def buscar_productos_por_nombre():
    producto_buscado = input("Ingrese el nombre del producto a buscar: ").capitalize()
    for clave, producto in inventario.items():
        if producto["nombre"] == producto_buscado:
            print(f"Producto encontrado exitosamente, esta es su información: ")
            mostrar_productos({clave: producto})
            return
        print("Producto no encontrado")

def eliminar_producto():
    mostrar_productos()
    codigo = 0
    while codigo <= 0:
            try:
                codigo = int(input("Ingrese el codigo del producto a eliminar: "))
                if codigo <=0:
                    print("Ingrese un numero mayor que 0")
            except ValueError:
                print("Ingrese un numero")
                codigo = 0
    producto_a_eliminar = inventario.get(codigo, "No encontrado")
    if producto_a_eliminar == "No encontrado":
        print("Codigo no encontrado")
    else:
        producto_a_eliminar = inventario.pop(codigo)
        print("Producto eliminado")
        mostrar_productos({codigo: producto_a_eliminar})



def menu_opciones():
    menu = True
    while menu:
        print("\nMenú de gestión de inventario.\n")
        opcion = input("\t***Menú***\n"
                       "\n 1. Registrar productos."
                       "\n 2. Mostrar los productos." 
                       "\n 3. Actualizar productos."
                       "\n 4. Eliminar productos." 
                       "\n 5. Buscar productos." 
                       "\n 6. Reportar de stock." 
                       "\n 7. Salir." 
                       "\n Ingrese la opción deseada (1-7) y presione enter, " 
                       "o escriba la palabra 'salir' para cerrar el programa.\n").lower()  
        if opcion == "1":
            registro_productos(contador_codigo)
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            buscar_productos_por_nombre()
        elif opcion == "6":
            reporte_bajo_stock()
        elif opcion == "7":
            print("Finalizando el programa... ")
            menu = False
        else:
            print("Opción incorrecta.")

menu_opciones()