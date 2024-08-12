# programa_principal.py

def menu_principal():
    while True:
        print("\nMenu Principal")
        print("1. Cargar datos en el archivo de pacientes")
        print("2. Cargar datos en el archivo de consultas")
        print("3. Búsqueda y visualización de datos")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            import cargar_pacientes
            cargar_pacientes.cargar_datos_pacientes()
        elif opcion == '2':
            import cargar_consultas
            cargar_consultas.cargar_datos_consultas()
        elif opcion == '3':
            import buscar_visualizar
            buscar_visualizar.busqueda_visualizacion()
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu_principal()
