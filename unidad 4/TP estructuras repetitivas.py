#Trabajo Practico Estructuras Repetitivas Unidad 4
#Punto 1: Imprimir los números del 0 al 100 en orden creciente

print("Números del 0 al 100")
i = 0
while i <= 100:
    print(i)
    i += 1
#Punto 2:  Determinar la cantidad de dígitos de un número

print("\nContador de dígitos (Sin excepciones)")
while True:
    entrada_str = input("Ingrese un número entero: ").strip()

    if entrada_str.startswith('-'):
        num_check = entrada_str[1:]
    else:
        num_check = entrada_str

    if num_check.isdigit():
        numero = int(entrada_str)
        break
    else:
        print("Error: Ingrese un número entero válido.")

if numero == 0:
    print("El número tiene 1 dígito.")
else:
    n_abs = abs(numero)
    contador = 0
    
    while n_abs > 0:
        n_abs //= 10 
        contador += 1
        
    print(f"El número {numero} tiene {contador} dígitos.")
    
#Punto 3: Sumar números enteros entre dos valores (excluyentes)

print("\nSuma de rango excluyente (Sin excepciones)")

while True:
    entrada_val1 = input("Ingrese el primer valor entero: ").strip()
    if entrada_val1.startswith('-'):
        val1_check = entrada_val1[1:]
    else:
        val1_check = entrada_val1
    
    if val1_check.isdigit():
        val1 = int(entrada_val1)
        break
    else:
        print("Error: Ingrese un número entero válido.")

while True:
    entrada_val2 = input("Ingrese el segundo valor entero: ").strip()
    if entrada_val2.startswith('-'):
        val2_check = entrada_val2[1:]
    else:
        val2_check = entrada_val2

    if val2_check.isdigit():
        val2 = int(entrada_val2)
        break
    else:
        print("Error: Ingrese un número entero válido.")

suma = 0
inicio = min(val1, val2) + 1
fin = max(val1, val2)

i = inicio
while i < fin:
    suma += i
    i += 1
    
if inicio >= fin:
    print("No hay números enteros entre los valores ingresados.")
else:
    print(f"La suma de los números entre {val1} y {val2} (excluidos) es: {suma}")


#Punto 4: Suma de números hasta que el usuario ingrese 0

print("\nSumador secuencial con parada en 0 (Sin excepciones)")
total_acumulado = 0

while True:
    entrada_str = input("Ingrese un número entero (0 para terminar y sumar): ").strip()
    if entrada_str.startswith('-'):
        num_check = entrada_str[1:]
    else:
        num_check = entrada_str
        
    if num_check.isdigit():
        numero = int(entrada_str)
        
        if numero == 0:
            break 
        
        total_acumulado += numero
        print(f"Número agregado. Total acumulado actual: {total_acumulado}")
        
    else:
        print("ADVERTENCIA: Entrada no válida. Por favor, ingrese un número entero.")

print(f"El total acumulado final es: {total_acumulado}")


#Punto 5: Juego de adivinanza de número aleatorio

import random 

print("\n--- 5. Juego de Adivinanza (0 a 9) (Sin excepciones) ---")

numero_secreto = random.randint(0, 9)
intentos = 0
adivinado = False

print("He generado un número secreto entre 0 y 9.")

while not adivinado:
    intentos += 1
    while True: 
        entrada_str = input(f"Intento #{intentos}. ¿Cuál es el número?: ").strip()
        if entrada_str.isdigit():
            suposicion = int(entrada_str)
            break
        else:
            print("ERROR: Ingrese solo un número entero.")
    if suposicion < 0 or suposicion > 9:
        print("Pista: El número debe estar entre 0 y 9.")
        intentos -= 1 
    elif suposicion == numero_secreto:
        adivinado = True
        print(f"¡Felicidades! Adivinaste el número {numero_secreto}.")
    elif suposicion < numero_secreto:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")
            
print(f"Fueron necesarios {intentos} intentos para acertar.")

#Punto 6:  Imprimir números pares del 0 al 100 (Decreciente)

print("\n6. Números Pares del 100 al 0 (Decreciente)")

i = 100
while i >= 0:
    print(i)
    i -= 2

#Punto 7: Calcular la suma de números entre 0 y N

print("\nSuma de 0 hasta N (Sin excepciones)")

# Validación para N positivo
while True:
    entrada_n = input("Ingrese un número entero positivo (N): ").strip()
    if entrada_n.isdigit():
        n = int(entrada_n)
        break
    else:
        print("Error: Ingrese un número entero válido y positivo.")
        
suma_total = 0
i = 0
while i <= n:
    suma_total += i
    i += 1
    
print(f"La suma de todos los números desde 0 hasta {n} es: {suma_total}")

#Punto 8: Conteo de 100 números (Pares, Impares, Positivos, Negativos)

print("\nConteo de 100 Números (Sin excepciones)")
CANTIDAD_A_PROCESAR = 100 

pares = 0
impares = 0
positivos = 0
negativos = 0

print(f"Ingrese {CANTIDAD_A_PROCESAR} números enteros.")

k = 0
while k < CANTIDAD_A_PROCESAR:
    
    
    while True: 
        entrada_str = input(f"Ingrese número {k + 1}: ").strip()
        if entrada_str.startswith('-'):
            num_check = entrada_str[1:]
        else:
            num_check = entrada_str
            
        if num_check.isdigit():
            num = int(entrada_str)
            break 
        else:
            print("Entrada no válida. Intente de nuevo.")
    if num != 0:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1

    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
        
    k += 1 

print("\nRESULTADOS DEL CONTEO")
print(f"Total de números procesados: {CANTIDAD_A_PROCESAR}")
print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")

#Punto 9: Cálculo de la media de 100 números

print("\nCálculo de la Media (Promedio) (Sin excepciones)")
CANTIDAD_A_PROCESAR = 100 

suma_total = 0
contador = 0

print(f"Ingrese {CANTIDAD_A_PROCESAR} números enteros para calcular su media.")

k = 0
while k < CANTIDAD_A_PROCESAR:
    
    # Bucle de validación de entrada
    while True: 
        entrada_str = input(f"Ingrese número {k + 1}: ").strip()
        
        # Lógica para manejar el signo negativo
        if entrada_str.startswith('-'):
            num_check = entrada_str[1:]
        else:
            num_check = entrada_str
            
        if num_check.isdigit():
            num = int(entrada_str)
            break 
        else:
            print("Entrada no válida. Intente de nuevo.")
            
    suma_total += num
    contador += 1
    k += 1 
        
print("\nRESULTADO DE LA MEDIA")
if contador > 0:
    media = suma_total / contador
    print(f"La suma total es: {suma_total}")
    # Formateo para dos decimales
    print(f"La media (promedio) de los {contador} números es: {media:.2f}") 
else:
    print("No se ingresaron números para calcular la media.")
    
#Punto 10: Invertir el orden de los dígitos de un número

print("\n--- 10. Invertir Dígitos (Sin excepciones) ---")


while True:
    entrada_n = input("Ingrese un número entero positivo: ").strip()
    if entrada_n.isdigit():
        numero_original = int(entrada_n)
        break
    else:
        print("Error: Ingrese un número entero válido y positivo.")

num_temp = numero_original
numero_invertido = 0

while num_temp > 0:
 
    digito = num_temp % 10
    
    numero_invertido = (numero_invertido * 10) + digito
    
    num_temp //= 10
    
print(f"El número original ({numero_original}) invertido es: {numero_invertido}")