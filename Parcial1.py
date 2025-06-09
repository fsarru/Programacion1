#Programación 1 - Primer Parcial
#1

i = 1
while i <= 2:
    print("Iteracion exterior:",i,end="")
    j =1
    bandera = True
    while bandera:
        print(" Iteración interior:",j,end=" ")
        j+=1
        if j != 2:
            bandera=False
    i = i+1

2#

for t in range (1,3):
    for n in range(1,4):
        print(t*n,end="")

3#

lista = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

lista[0] = 1
lista[1] = 1
lista[2] = 1
lista[3] = 2
lista[4] =1

n = 5
r = 0

if n == 0:
    r = 0
else:
    r = lista[n-1]
    for i in range(n-1,0,-1):
        r += lista[i-1]

print(r)

4#

f = "HolaMundoCruel"
r = f
l = len(f)

for i in range(0,l+1,5):
    r = f[i:l]

print(r)

5#

for n in range(1,11):
    bandera = False
    d= 0

    for c in range(1, n+1):
        if n % c == 0:
            d += 1

            if d <= 2:
                bandera = True
            else:
                bandera = False

    if bandera:
        print(n,end="")

6#

N = 5
A = [0] * N
B = [0] * N

for i in range(N):
    A[i] = i+i+i

for i in range(N):
    B[i] = i*2

contador = 0
for i in range(N):
    if A[0] == A[i] and A[0] == B[i]:
        contador +=1
        N = N - contador

resultado = str(contador)

if A[0] == 1:
    resultado = "VERDADERO"
elif A[0] == 2:
    resultado = "2"
elif A[0] == 3:
    resultado = "FALSO"
print(resultado)


7#

num1 = 3
num2 = 7
num3 = 4

if num2 % 2 == 0:
    x = num2 *2
else: 
    x = 3 * num2

if x % 2 == 0:
    t = x+num3
else:
    t = x -num3

if t > 10:
    resultado_final = t *num1
else:
    resultado_final = t + num1

print(f"Resultado final: {resultado_final}")

8#

contador = 1
suma = 0
bandera = True
num1 = int(input("Ingrese un valor N°1: "))

while bandera:
    num2 = int(input("Ingrese un valor N°2: "))
    suma = suma + num2
    contador = contador +1

    while contador <= num1:
        print(suma,end=",")
        bandera = False
        if contador == num1:
            bandera = True
        break

9#

num1 = 3
vector = [4,6,1]

mayor = vector[0]

for i in range (1,num1):
    if vector[i] > mayor:
        mayor = vector[i]

print(mayor)

10#

dia = int(input("Introduce el valor N°1: "))
mes = int(input("Introduce el valor N°2: "))
anio= int(input("Introduce el valor N°3: "))

if mes in [1,3,5,6,7,8,10,12]:
    dd = 31
elif mes in [4,6,9,11]:
    dd = 30
elif mes == 2:
    if(anio %4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        dd = 29
    else:
        dd = 28
else:
    print("A")
    dd = -1

if dd != -1:
    if dia <1 or dia > dd:
        print("B")
    elif mes <1 or mes > 12:
        print("C")
    else:
        print("D")