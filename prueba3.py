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