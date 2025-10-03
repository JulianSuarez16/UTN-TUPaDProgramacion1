#Trabajo Practico condicionales
#Punto1

edad = int(input("ingresa tu edad: "))

if edad >= 18:
    print("Es mayor de edad.")
    
#punto 2 

nota = float(input("ingresa tu nota: "))

if nota >= 6:
    print("Aprobado.")
else:
    print("Desaprobado")
    
#punto 3

numero = int(input("ingrese un numero: "))
 
if numero % 2 == 0:
    print("ha ingresado un numero par")
else:
    print("Por favor, ingrese un numero par.")
    
#punto 4

edad = int(input("ingresa tu edad: "))
if edad < 12:
    print("Usted corresponde a la categoria NIÑO/A.")
elif edad >= 12 and edad < 18:
    print("Usted pertenece a la categria ADOLESCENTE.")
elif edad >= 18 and edad < 30:
    print("usted pertenece a la categoria ADULTO/A JOVEN.")
else:
    print("Usted pertenece a la categoria ADULTO/A")

#punto 5 

contraseña = input("Ingrese su contraseña: ")

if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor introduzca una contraseña entre 8 y 14 caracteres")
    
#punto 6

import random 
import statistics
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
print("Lista de numeros: (numeros_aleatorios)\n")

media = statistics.mean(numeros_aleatorios)
mediana = statistics.median(numeros_aleatorios)
moda = statistics.mode(numeros_aleatorios)

if media > mediana and mediana > moda:
    print("hay sesgo positivo")
elif media < mediana and mediana< moda:
    print("hay sesgo negativo")
elif media == moda and media == mediana:
    print("no hay sesgo")
else:
    pass

#punto 7 

palabra = (input("ingresa una palabra: "))
longitud = len(palabra)

if longitud > 0:
    ultimo_caracter = palabra[longitud - 1]
    
if (ultimo_caracter == 'a' or ultimo_caracter == 'e' or 
        ultimo_caracter == 'i' or ultimo_caracter == 'o' or 
        ultimo_caracter == 'u' or ultimo_caracter == 'A' or 
        ultimo_caracter == 'E' or ultimo_caracter == 'I' or 
        ultimo_caracter == 'O' or ultimo_caracter == 'U' or
        ultimo_caracter == 'á' or ultimo_caracter == 'é' or
        ultimo_caracter == 'í' or ultimo_caracter == 'ó' or
        ultimo_caracter == 'ú' or ultimo_caracter == 'Á' or 
        ultimo_caracter == 'É' or ultimo_caracter == 'Í' or 
        ultimo_caracter == 'Ó' or ultimo_caracter == 'Ú'):
    print(f"{palabra}!")
else:
    print(f"{palabra}")
    
    
#punto 8

nombre = (input("ingrese su nombre: "))

print("ingrese 1 si quiere su nombre en mayusculas")
print("ingrese 2 si quiere su nombre en minusculas")
print("ingrese 3 si quiere su nombre con la primer letra en mayusculas")

opcion_elegida = input("Elija la opcion deseada: ")

if opcion_elegida == '1':
    nombre_final = nombre.upper()
    print(f"Su nombre en mayusculas es: {nombre_final}")
elif opcion_elegida == '2':
    nombre_final = nombre.lower()
    print(f"Su nombre en minusculas es: {nombre_final}")
elif opcion_elegida == '3':
    nombre_final = nombre.title()
    print(f"Su nombre con la primer letra en mayusculas es: {nombre_final}")
else:
    pass

#punto 9

magnitud_terremoto = int(input("Por favor, introduce la magnitud del terremoto: "))

if magnitud_terremoto < 3:
    print("Muy leve (imperceptible)")
    
elif magnitud_terremoto < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud_terremoto < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud_terremoto < 6:
    print( "Fuerte (puede causar daños en estructuras débiles)")
elif magnitud_terremoto < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

#punto 10

hemisferio = (input("¿En que hemisferio del mundo te encontras?(N/S): "))
mes = int(input("Introduce el número del mes (1=Ene, 2=Feb, ..., 12=Dic): "))
dia = int(input("Introduce el día del mes: "))

if (mes == 12 and dia >= 21) or mes == 1 or mes == 2 or (mes == 3 and dia <= 20):
    if hemisferio == 'N':
        print("Usted se encuentra en invierno")
    else:
        print("Usted se encuentra en verano")
elif (mes == 3 and dia >= 21) or mes == 4 or mes == 5 or (mes == 6 and dia <= 20):
    if hemisferio == 'N':
        print("Usted esta en primavera")
    else:
        print("usted esta en otoño")
elif (mes == 6 and dia >= 21) or mes == 7 or mes == 8 or (mes == 9 and dia <= 20):
    if hemisferio == 'N':
        print("Usted esta en verano")
    else:
        print("usted esta en invierno")
else:
    if hemisferio == 'N':
        print("Usted esta en otoño")
    else:
        print("Usted esta en primavera")
