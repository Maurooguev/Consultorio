# cargar_consultas.py

def verificar_existencia_paciente(numero_historia, archivo_pacientes):
    # Verificar si el paciente con el número de historia clínica existe en el archivo de pacientes
    try:
        archivo = open(archivo_pacientes, 'r', encoding='utf-8-sig')
        linea = archivo.readline().strip()
        while linea:
            if linea.split(',')[0] == numero_historia:
                archivo.close()
                return True
        linea = archivo.readline().strip()  # Leer la proxima linea
        archivo.close()
    except FileNotFoundError:
        pass 
    return False

def cargar_datos_consultas():
    archivo_consultas = "consultas.txt"
    archivo_pacientes = "pacientes.txt"
    
    # Solicitar datos de la consulta al usuario
    numero_historia = input("Ingrese el número de historia clínica: ").strip()
    diagnostico = input("Ingrese el diagnóstico: ").strip().upper()
    fecha = input("""Ingrese la fecha en formato "AAAAMMDD" (únicamente los números): """).strip() 
    
    # Verificar si el paciente existe
    if not verificar_existencia_paciente(numero_historia, archivo_pacientes):
        print("Error: El paciente no existe.")
        return
    
    # Verificar la validez de la fecha ingresada
    if len(fecha) != 8 or not fecha.isdigit():
        print("Error: La fecha ingresada no es válida.")
        return
    
    anio = int(fecha[0:4])
    mes = int(fecha[4:6])
    dia = int(fecha[6:8])
    
    if mes < 1 or mes > 12:
        print("Error: El mes ingresado no es válido.")
        return
    
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if mes == 2:
        if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
            if dia > 29:
                print("Error: El día ingresado no es válido para febrero en un año bisiesto.")
                return
        elif dia > 28:
            print("Error: El día ingresado no es válido para febrero en un año no bisiesto.")
            return
    else:
        if dia < 1 or dia > dias_por_mes[mes - 1]:
            print("Error: El día ingresado no es válido para el mes especificado.")
            return
    try:
        # Abrir el archivo de consultas en modo append y escribir la nueva consulta
        archivo = open(archivo_consultas, 'a', encoding='utf-8')
        archivo.write(f"{numero_historia},{diagnostico},{fecha}\n")
        archivo.close()
        print("Datos de la consulta cargados exitosamente.")
    except FileNotFoundError:
        print(f"No se pudo abrir el archivo {archivo_consultas}.")

if __name__ == "__main__":
    cargar_datos_consultas()

