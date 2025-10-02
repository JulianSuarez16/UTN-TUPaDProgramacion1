#Trabajo Practico Secuenciales.
#programa1

print("hola mundo")

#Programa 2

nombre = input("¿como te llamas?")
print(f"hola {nombre}")

#Programa3

nombre = input("¿como es tu nombre?")
apellido = input("¿como es tu apellido?")
edad = input("¿cuantos años tenes?")
lugarderesidencia = input("¿cual es tu pais de residencia?")

print(f" hola soy {nombre} {apellido} tengo {edad} años y vivo en {lugarderesidencia}.")

#programa 4

radio = float(input("Por favor, introduce el radio del círculo: "))
pi = 3.14
area = pi * (radio ** 2)
perimetro = 2 * pi * radio
print(f"Radio ingresado: {radio}")
print(f"El Área del círculo es: {area}")
print(f"El Perímetro del círculo es: {perimetro}")

 #Programa 5

segundos = int(input("Introduce la cantidad total de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas} horas.")

#Programa 6

numero = int(input("Introduce el número de la tabla que quieres imprimir: "))
print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")

#Programa 7

numero = int(input("Introduce un numero entero que no sea el 0: "))
numero_2 = int(input("Introduce un numero entero que no sea el 0: "))
print(f"{numero} + {numero_2} = {numero + numero_2}")
print(f" {numero} x {numero_2} = {numero * numero_2}")
print(f"{numero} - {numero_2} = {numero - numero_2}")
print(f"{numero} / {numero_2} = {numero / numero_2}")

#Programa 8

altura = float(input("introduce cual es tu altura exacta en metros: "))
peso = float(input("introduce cual es tu peso exacto en kg: "))
imc = peso / (altura ** 2)
print(f"tu indice de masa corporal es: {imc}")

#Programa 9

temperatura_celsius = float(input("Introduce la temperatura en grados Celsius: "))
temperatura_fahrenheit = (temperatura_celsius * 9 / 5) + 32
print(f"{temperatura_celsius} °C equivalen a {temperatura_fahrenheit} °F")


#Programa 10

numero = float(input("Introduce un numero: "))
numero_2 = float(input("Introduce un numero: "))
numero_3 = float(input("Introduce un numero: "))
print(f"El promedio de los 3 numeros es = {numero + numero_2 + numero_3 / 3}")