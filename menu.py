import registro_prod, mostrar_prod, buscar_prod, bajoStock_prod

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
        registro_prod.registrar_producto()
    elif opcion == '2':
        buscar_prod.buscar_producto()
    elif opcion == '3':
        bajoStock_prod.reporte_bajoStock()
    elif opcion == '4':
        inventario.eliminar_producto()
    elif opcion == '5':
        mostrar_prod.mostrar_productos()
    elif opcion == '6':
        bajoStock_prod.reporte_bajoStock()
    elif opcion == '7':
        print("Saliendo del sistema...")
        break
    else:
        
        print("\n\nOpción no válida. Intente de nuevo.")