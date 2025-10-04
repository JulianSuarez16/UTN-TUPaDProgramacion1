# Actividad 1: Notas de estudiantes
notas = [8.5, 7.0, 9.5, 6.0, 10.0, 5.5, 7.5, 8.0, 9.0, 6.5]

print("--- Notas de los 10 estudiantes ---")

print("\nLista completa de notas:")
for nota in notas:
    print(nota)

suma_notas = 0
for nota in notas:
    suma_notas += nota

cantidad_estudiantes = len(notas)
promedio = suma_notas / cantidad_estudiantes

print(f"\nEl promedio de las notas es: {promedio:.2f}")

nota_mas_alta = max(notas)
nota_mas_baja = min(notas)

print(f"La nota más alta es: {nota_mas_alta}")
print(f"La nota más baja es: {nota_mas_baja}")

# Actividad 2: 

# 1. Pedir al usuario que cargue 5 productos en una lista.
lista_productos = []
print("--- Carga de 5 Productos ---")
for i in range(5):
    producto = input(f"Ingrese el nombre del producto {i+1}: ")
    lista_productos.append(producto)


print("\nLista de productos ingresada (original):")

for p in lista_productos:
    print(f"- {p}")

lista_ordenada = sorted(lista_productos)

print("\nLista de productos ordenada alfabéticamente:")

for p in lista_ordenada:
    print(f"-> {p}")

producto_a_eliminar = input("\nIngrese el nombre exacto del producto que desea ELIMINAR de la lista: ")


if producto_a_eliminar in lista_productos:
    
    lista_productos.remove(producto_a_eliminar)
    print(f"\nEl producto '{producto_a_eliminar}' ha sido eliminado exitosamente.")
else:
    print(f"\nError: El producto '{producto_a_eliminar}' no se encontró en la lista. No se realizó ninguna eliminación.")

print("\nLista de productos final actualizada:")

for p in lista_productos:
    print(f"-> {p}")

#actividad 3:

import random

numeros_aleatorios = [random.randint(1, 100) for _ in range(15)]

pares = [num for num in numeros_aleatorios if num % 2 == 0]
impares = [num for num in numeros_aleatorios if num % 2 != 0]

print("Lista original:")
print(numeros_aleatorios)
print("Lista de pares:")
print(pares)
print("Lista de impares:")
print(impares)

print("Cantidad de números en la lista de pares:")
print(len(pares))
print("Cantidad de números en la lista de impares:")
print(len(impares))

#actividad 4:

datos = [1, 3, 5, 5, 3, 7, 1, 9, 5, 3]

lista_sin_repetidos = list(set(datos))

print(lista_sin_repetidos)

#actividad 5:

estudiantes = [
    "Ana", "Beto", "Carlos", "Diana",
    "Elias", "Fernanda", "Gabriel", "Helena"
]

print("Lista inicial de estudiantes:")
print(estudiantes)

print("\n¿Qué acción desea realizar?")
accion = input("Escriba 'agregar' para añadir un estudiante o 'eliminar' para quitar uno: ").lower()

if accion == 'agregar':
    nuevo_estudiante = input("Ingrese el nombre del nuevo estudiante: ")
    estudiantes.append(nuevo_estudiante.capitalize())
    print(f"\n'{nuevo_estudiante.capitalize()}' ha sido agregado.")
elif accion == 'eliminar':
    nombre_a_eliminar = input("Ingrese el nombre del estudiante a eliminar: ")
    nombre_a_eliminar_capitalizado = nombre_a_eliminar.capitalize()
    if nombre_a_eliminar_capitalizado in estudiantes:
        estudiantes.remove(nombre_a_eliminar_capitalizado)
        print(f"\n'{nombre_a_eliminar_capitalizado}' ha sido eliminado.")
    else:
        print(f"\nError: '{nombre_a_eliminar_capitalizado}' no se encuentra en la lista.")
else:
    print("\nAcción no válida. La lista no ha sido modificada.")

print("\nLista final actualizada de estudiantes:")
print(estudiantes)

#actividad 6:

numeros = [10, 20, 30, 40, 50, 60, 70]
ultimo_elemento = numeros.pop()
numeros.insert(0, ultimo_elemento)

print(numeros)

#actividad 7:
temperaturas_semana = [
    [15, 25],  # Lunes
    [17, 28],  # Martes
    [14, 26],  # Miércoles
    [16, 30],  # Jueves
    [18, 27],  # Viernes
    [20, 32],  # Sábado
    [19, 29]   # Domingo
]


dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
minimas = [dia[0] for dia in temperaturas_semana]
maximas = [dia[1] for dia in temperaturas_semana]
promedio_minimas = sum(minimas) / len(minimas)
promedio_maximas = sum(maximas) / len(maximas)

print("Temperaturas semanales (Min/Max):")
for i, (min_temp, max_temp) in enumerate(temperaturas_semana):
    print(f"{dias_semana[i]}: {min_temp}°C / {max_temp}°C")

print("\n---")
print(f"Promedio de temperaturas mínimas: {promedio_minimas:.2f}°C")
print(f"Promedio de temperaturas máximas: {promedio_maximas:.2f}°C")

amplitudes = [maxima - minima for minima, maxima in temperaturas_semana]
maxima_amplitud = max(amplitudes)
indice_mayor_amplitud = amplitudes.index(maxima_amplitud)
dia_mayor_amplitud = dias_semana[indice_mayor_amplitud]

print("\n---")
print(f"La mayor amplitud térmica ({maxima_amplitud}°C) se registró el día: {dia_mayor_amplitud}")

#actividad 8:
notas = [
    [85, 78, 92],  # Estudiante 1
    [90, 88, 76],  # Estudiante 2
    [75, 95, 80],  # Estudiante 3
    [88, 70, 91],  # Estudiante 4
    [79, 83, 85]   # Estudiante 5
]

estudiantes = ["Estudiante 1", "Estudiante 2", "Estudiante 3", "Estudiante 4", "Estudiante 5"]
materias = ["Materia 1", "Materia 2", "Materia 3"]

print("--- Promedio de cada estudiante ---")
promedios_estudiantes = []
for i, nota_estudiante in enumerate(notas):
    promedio = sum(nota_estudiante) / len(nota_estudiante)
    promedios_estudiantes.append(promedio)
    print(f"{estudiantes[i]}: {promedio:.2f}")

print("\n--- Promedio de cada materia ---")
num_estudiantes = len(notas) # 5
num_materias = len(notas[0]) # 3

promedios_materias = []
for j in range(num_materias):
    suma_notas_materia = 0
    for i in range(num_estudiantes):
        suma_notas_materia += notas[i][j]
    promedio_materia = suma_notas_materia / num_estudiantes
    promedios_materias.append(promedio_materia)

    print(f"{materias[j]}: {promedio_materia:.2f}")

#actividad 9:

def mostrar_tablero(tablero):
    """Muestra el tablero en un formato legible."""
    print("  0 1 2")  
    for i in range(3):
        print(f"{i} {' '.join(tablero[i])}")
tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

jugador_actual = "X"
turno = 0
max_turnos = 9 

print("--- ¡Comienza el Ta-Te-Tí! ---")
mostrar_tablero(tablero)
while turno < max_turnos:
    print(f"\nTurno de {jugador_actual}")
    while True:
        try:
            entrada = input("Ingrese la posición (ej: 1,2 para fila 1, columna 2): ")
            fila, columna = map(int, entrada.split(','))
            if not (0 <= fila <= 2 and 0 <= columna <= 2):
                print("Error: Los valores de fila y columna deben estar entre 0 y 2. Intente de nuevo.")
                continue
            if tablero[fila][columna] != "-":
                print("Error: Esa casilla ya está ocupada. Intente de nuevo.")
                continue
            break

        except ValueError:
            print("Error: Formato incorrecto. Debe ingresar dos números separados por coma (ej: 1,2). Intente de nuevo.")
        except IndexError:
            print("Error: Los valores de fila y columna están fuera de rango. Intente de nuevo.")

    tablero[fila][columna] = jugador_actual
    mostrar_tablero(tablero)
    if jugador_actual == "X":
        jugador_actual = "O"
    else:
        jugador_actual = "X"

    turno += 1
print("\n¡Juego Terminado!")

#actividad 10:

ventas = [
    #  Lun Mar Mie Jue Vie Sab Dom (Ventas del Producto 1)
    [10, 15, 8, 12, 20, 35, 25], # Producto A (índice 0)
    [5, 10, 15, 5, 8, 10, 12],   # Producto B (índice 1)
    [25, 30, 20, 40, 35, 50, 45],# Producto C (índice 2)
    [18, 12, 14, 16, 22, 10, 15] # Producto D (índice 3)
]

productos = ["Producto A", "Producto B", "Producto C", "Producto D"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
print("--- Total vendido por cada producto ---")
ventas_por_producto = []
for i, ventas_producto in enumerate(ventas):
    total = sum(ventas_producto)
    ventas_por_producto.append(total)
    print(f"{productos[i]}: {total} unidades")

num_dias = len(ventas[0])
ventas_por_dia = []

for j in range(num_dias):
    suma_dia = 0
    for i in range(len(ventas)):
        suma_dia += ventas[i][j]
    ventas_por_dia.append(suma_dia)
max_ventas_dia = max(ventas_por_dia)
indice_max_dia = ventas_por_dia.index(max_ventas_dia)
dia_mayor_ventas = dias_semana[indice_max_dia]

print("\n--- Día con mayores ventas totales ---")
print(f"El día con mayores ventas totales fue el {dia_mayor_ventas} con {max_ventas_dia} unidades vendidas.")
max_ventas_producto = max(ventas_por_producto)
indice_max_producto = ventas_por_producto.index(max_ventas_producto)
producto_mas_vendido = productos[indice_max_producto]

print("\n--- Producto más vendido en la semana ---")
print(f"El producto más vendido fue el {producto_mas_vendido} con un total de {max_ventas_producto} unidades.")