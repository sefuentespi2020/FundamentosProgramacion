# Programa: Clasificación de Jornada Laboral Semanal (Problema 5)
# Curso: Fundamentos de Programación (213022) - Fase 5

def mostrar_matriz(matriz):
    print("\n--- MATRIZ DE HORAS REGISTRADAS ---")
    print("Recurso | Lun | Mar | Mié | Jue | Vie")
    for fila in matriz:
        print(f"{fila[0]} | {fila[1]} | {fila[2]} | {fila[3]} | {fila[4]} | {fila[5]}")

def calcular_y_clasificar_jornada(horas_dias):
    total_horas = 0
    for horas in horas_dias:
        total_horas = total_horas + horas
    
    if total_horas > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario estándar"
        
    return total_horas, clasificacion

def mostrar_calculos_finales(matriz):
    print("\n--- REPORTE SEMANAL DE HORAS TRABAJADAS ---")
    for fila in matriz:
        nombre_recurso = fila[0]
        horas_semana = fila[1:6]
        total, estado = calcular_y_clasificar_jornada(horas_semana)
        print(f"Recurso: {nombre_recurso} | Total Horas: {total} | Clasificación: {estado}")

def menu():
    # Matriz con 4 recursos: [Nombre del recurso, Lunes, Martes, Miércoles, Jueves, Viernes]
    matriz_horas = [
        ["Carlos Mendoza", 8, 9, 8, 9, 8],
        ["Laura Gómez", 8, 8, 8, 8, 8],
        ["Andrés Torres", 9, 9, 9, 9, 8],
        ["Sofía Ramírez", 7, 8, 8, 7, 8]
    ]
    
    opcion = ""
    while opcion != "3":
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Mostrar matriz registrada")
        print("2. Mostrar cálculos finales y clasificación")
        print("3. Salir")
        opcion = input("Seleccione una opción (1-3): ")
        
        if opcion == "1":
            mostrar_matriz(matriz_horas)
        elif opcion == "2":
            mostrar_calculos_finales(matriz_horas)
        elif opcion == "3":
            print("Saliendo del programa...")
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecución del menú principal
menu()
