#buscar_visualizar.py

def busqueda_visualizacion():
    archivo_pacientes = "pacientes.txt"
    archivo_consultas = "consultas.txt"
    
    nombre_busqueda = input("Ingrese el nombre del paciente: ").strip().upper()
    
    pacientes = {}  
    try:
        # Leer el archivo de pacientes y cargar los datos en un diccionario
        archivo = open(archivo_pacientes, 'r', encoding='utf-8-sig')
        linea = archivo.readline().strip()
        while linea:
            numero_historia, nombre_apellido, prepaga = linea.split(',')
            pacientes[numero_historia] = (nombre_apellido, prepaga)
            linea = archivo.readline().strip()  # Leer la próxima línea
        archivo.close()
    except FileNotFoundError:
        print("No se han cargado datos de pacientes.")
        return
    
    # Filtrar los pacientes cuyo nombre contiene la cadena ingresada
    pacientes_encontrados = {k: v for k, v in pacientes.items() if nombre_busqueda in v[0]}  
    
    if not pacientes_encontrados:
        print("No se encontraron pacientes con ese nombre.")
        return
    
    # Mostrar la lista de pacientes encontrados
    print("\nPacientes encontrados:")
    for i, (numero_historia, (nombre_apellido, _)) in enumerate(pacientes_encontrados.items(), 1):
        print(f"{i}. {nombre_apellido} (Historia Clínica: {numero_historia})")
    
    # Solicitar al usuario seleccionar un paciente por su número en la lista
    seleccion = int(input("\nSeleccione un paciente por número: ")) - 1
    if seleccion < 0 or seleccion >= len(pacientes_encontrados):
        print("Error: Selección inválida.")
        return
    
    # Obtener el número de historia clínica del paciente seleccionado
    paciente_seleccionado = list(pacientes_encontrados.keys())[seleccion]
    
    print(f"\nConsultas para el paciente {pacientes[paciente_seleccionado][0]} (Historia Clínica: {paciente_seleccionado}):")
    
    consultas = []                                             
    try:
        # Leer el archivo de consultas y filtrar las consultas del paciente seleccionado
        archivo = open(archivo_consultas, 'r', encoding='utf-8-sig')
        linea = archivo.readline().strip()
        while linea:
            numero_historia, diagnostico, fecha = linea.split(',')
            if numero_historia == paciente_seleccionado:
                consultas.append((numero_historia, diagnostico, fecha))
            linea = archivo.readline().strip()  # Leer la próxima línea
        archivo.close()
    except FileNotFoundError:
        print("No se han cargado datos de consultas.")
        return
    
    if not consultas:
        print("El paciente no tiene consultas realizadas.")
        return
    
    # Crear matriz de consultas y ordenar por fecha
    matriz_consultas = []
    for i in range(len(consultas)):
        matriz_consultas.append([''] * 3)  # Suponiendo 3 columnas: número de historia clínica, diagnóstico y fecha
    
    # Llenar la matriz de consultas con los datos de las consultas
    for i, consulta in enumerate(consultas):
        for j in range(len(consulta)):
            matriz_consultas[i][j] = consulta[j]
    
    # Ordenar la matriz de consultas por fecha (asumiendo que la fecha es el tercer elemento)
    matriz_consultas.sort(key=lambda x: x[2])
    
    # Función recursiva para mostrar la matriz de consultas
    def mostrar_consultas_recursivamente(matriz, i=0):
        if i >= len(matriz):
            return
        print(f"Número de Historia Clínica: {matriz[i][0]}, Diagnóstico: {matriz[i][1]}, Fecha: {matriz[i][2]}")
        mostrar_consultas_recursivamente(matriz, i + 1)
    
    print("\nConsultas ordenadas por fecha:")
    mostrar_consultas_recursivamente(matriz_consultas)


if __name__ == "__main__":
    busqueda_visualizacion()



