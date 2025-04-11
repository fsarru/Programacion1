# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range (0,101):
    print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

num = int(input("Ingrese un número entero:"))
digitos = 0
while num > 0:
    num = num // 10
    digitos += 1
print(f"El número ingresado tiene {digitos} digitos.")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

suma = 0
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

for i in range (num1, num2+1):
    suma += i
print(f"La suma de los números entre {num1} y {num2} es {suma}".)

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

num = int(input("Ingrese un número: "))
contador = 0
suma = 0

while num != 0:
    contador += 1
    suma += num
    num = int(input("Ingrese un número: "))
print(f"El total de números ingresados es {contador} y la suma acumulada es {suma}.")


# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

aleatorio = random.randint(0,9)
num = int(input("Intente adivinar el número entre 0 y 9: "))
contador = 1

while num != aleatorio:
    contador += 1
    num = int(input("Equivocado! Pruebe de nuevo: "))
print(f"Correcto! El número aleatorio es {aleatorio} y te tomó {contador} intentos adivinarlo.")


# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

for i in range (100,1,-2):
    print(i)


# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario

suma = 0
num = int(input("Ingrese un número: "))

for i in range (0,num+1):
    suma += i
print(suma)

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).


pos = 0
neg = 0
par = 0
impar = 0


for i in range (100):
    num = int(input(f"Ingrese un número:"))
    if num > 0:
        pos += 1
    else: 
        neg += 1

    if num % 2 == 0:
        par += 1
    else:
        impar +=1

print(f"Cantidad de números pares: {par}")
print(f"Cantidad de números impares: {impar}")
print(f"Cantidad de números positivos: {pos}")
print(f"Cantidad de números negativos: {neg}")


# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

#from statistics import mean

suma = 0

for i in range (100):
    num = int(input(f"Ingrese un número:"))
    suma += num
print("La meadia de los números ingresados es: " ,suma/100)


# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

inv= 0
num = int(input("Ingrese un número: "))

while num > 0:
    ultimo = num % 10
    inv = (inv * 10) + ultimo
    num //= 10

print(f"El número invertido es: {inv}")
