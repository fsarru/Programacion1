

num = int(input("Ingrese un número: "))
contador = 0
suma = 0

while num != 0:
    contador += 1
    suma += num
    num = int(input("Ingrese un número: "))
print(f"El total de números ingresados es {contador} y la suma acumulada es {suma}.")