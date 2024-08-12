# cargar_pacientes.py

def verificar_unicidad_historia(numero_historia, archivo_pacientes):
    # Verificar si el número de historia clínica es único en el archivo de pacientes
    try:
        archivo = open(archivo_pacientes, 'r', encoding='utf-8-sig')
        linea = archivo.readline().strip()
        while linea:
            if linea.split(',')[0] == numero_historia:
                archivo.close()
                return False
            linea = archivo.readline().strip()
        archivo.close()
        
    except FileNotFoundError:
        # Si el archivo no existe, no hay duplicados
        pass 
    return True

def cargar_datos_pacientes():
    archivo_pacientes = "pacientes.txt"
    
    numero_historia = input("Ingrese el número de historia clínica: ").strip()
    nombre_apellido = input("Ingrese el nombre y apellido del paciente: ").strip().upper()
    prepaga = input("Ingrese la prepaga u obra social: ").strip()
    

    if not verificar_unicidad_historia(numero_historia, archivo_pacientes):
        print("Error: El número de historia clínica ya existe.")
        return
    
    # Verificar que el número de historia clínica sea válido (número)
    try:
        int(numero_historia) 
    except ValueError:
        print("Error: El número de historia clínica no es un número válido.")
        return
    
    try:	
        # Abrir el archivo de pacientes en modo append y escribir los datos del nuevo paciente
        archivo = open(archivo_pacientes, 'a', encoding='utf-8')
        archivo.write(f"{numero_historia},{nombre_apellido},{prepaga}\n")
        archivo.close()
    
        print("Datos del paciente cargados exitosamente.")
        
    except FileNotFoundError:
        print(f"No se pudo abrir el archivo {archivo_pacientes}.")

if __name__ == "__main__":
    cargar_datos_pacientes()

