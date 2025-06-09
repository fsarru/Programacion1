# 1-Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

def imprimir_hola_mundo():
    return("Hola Mundo!")

print(imprimir_hola_mundo())


# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver:
# “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.


def saludar_usuario(nombre):
    return(f"Hola {nombre}! ")

a = input("Ingrese el nombre: ")

print(saludar_usuario(a))

# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir
# los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
    return(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

a = input("Ingrese su nombre: ")
b = input("Ingrese su apellido: ")
c = input("Ingrese su edad: ")
d = input("Ingrese su lugar de residencia: ")

print(informacion_personal(a,b,c,d))

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio
# como parámetro y devuelva el área del círculo. calcular_perimetro_
# circulo(radio) que reciba el radio como parámetro y devuelva
# el perímetro del círculo. Solicitar el radio al usuario y llamar ambas
# funciones para mostrar los resultados.

def calcular_area_circulo(radio):
    return(3.14*(radio*radio))

def calcular_perimetro_circulo(radio):
    return(3.14*(radio*2))

a = float(input("Ingrese el radio: "))

print(calcular_area_circulo(a))
print(calcular_perimetro_circulo(a))

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar
# el resultado usando esta función.

def segundos_a_horas(segundos):
    return((segundos/60)/60)

a = int(input("Ingrese la cantidad de segundos: "))

print(f"{a} segundos equivalen a {segundos_a_horas(a)} horas.")

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i
    return(f"{numero} x {i} = {resultado}")

a = int(input("Ingrese el número para la tabla de multiplicar: "))
print(tabla_multiplicar(a))


# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado
# de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados
# de forma clara.

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b

    division = a / b if b != 0 else "Error: División por cero"
    return (suma, resta, multiplicacion, division)


num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

resultados = operaciones_basicas(num1, num2)

print(f"Los números ingresados son: {num1} y {num2}")
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")



# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función
# para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    return(peso/(altura*altura))

a = float(input("Ingrese su peso en KG: "))
b = float(input("Ingrese su altura en Metros: "))

print(f"Dado que su peso es {a} Kgs. y su altura es {b} mts, su IMC es de {calcular_imc(a,b)}.")

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

def celsius_a_fahrenheit(celsius):
    return((celsius*(9/5))+32)

a = float(input("Ingrese la temperatura en Celsius: "))

print(f"{a} Celsius equivale a {celsius_a_fahrenheit(a)} fahrenheit. ")

# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.

def calcular_promedio(a, b, c):
    return((a+b+c)/3)

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

print(f"El promedio de {num1} + {num2} + {num3} es {calcular_promedio(num1,num2,num3)}")