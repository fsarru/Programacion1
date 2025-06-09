# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función 
# para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario.

def factorial(a):
    if a == 0:
        return 1
    else:
        return a * factorial(a-1)
    
a = int(input("Ingrese un número: "))
print(f"El factorial de {a} es {factorial(a)}")

# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. 
# Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

def fibo(a):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    else:
        return fibo(a-1)+(fibo(a-2))
    
a = int(input("Ingrese la posición a consultar: "))

for i in range(a):
    print(f"En la posición {i} obtenemos el valor de Fibonacci {fibo(i)}")



# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, 
# utilizando la fórmula 𝑛𝑚= 𝑛∗𝑛(𝑚−1). Prueba esta función en un algoritmo general.

def exponente(base, potencia):
    if potencia < 0:
        return("El exponente no puede ser negativo.")
    elif potencia == 0:
        return 1
    elif potencia == 1:
        return base
    else:
        return base * exponente(base, potencia - 1)

print(exponente(5,4))


# 4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal 
# y devuelva su representación en binario como una cadena de texto.

def a_binario(n):
    if n <= 1:
        return str(n)
    else:
        return a_binario(n // 2) + str(n % 2)

decimal = int(input("Ingrese el decimal para convertirlo a binario: "))

print(f"El binario de {decimal} es: {a_binario(decimal)}")

# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, 
# y devuelva True si es un palíndromo o False si no lo es.
# Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed().

def palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return palindromo(palabra[1:-1])

print(palindromo(palabra))

# 6) Escribí una función recursiva en Python llamada suma_digitos(n) 
# que reciba un número entero positivo y devuelva la suma de todos sus dígitos.
# Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.
# Ejemplos:
# suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
# suma_digitos(9) → 9
# suma_digitos(305) → 8 (3 + 0 + 5)

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)
    
n = int(input("Ingese un valor para sumar sus dígitos: "))

print(f"La suma de los dígitos que componen {n} es {suma_digitos(n)}")



# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), 
# y así sucesivamente hasta llegar al último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva el total de 
# bloques que necesita para construir toda la pirámide.
# Ejemplos:
# contar_bloques(1) → 1 (1)
# contar_bloques(2) → 3 (2 + 1)
# contar_bloques(4) → 10 (4 + 3 + 2 + 1)

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n+contar_bloques(n-1)

print(contar_bloques(13))


# 8) Escribí una función recursiva llamada contar_digito(numero, digito) 
# que reciba un número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.
# Ejemplos:
# contar_digito(12233421, 2) → 3
# contar_digito(5555, 5) → 4

def contar_digito(numero,digito):
    if numero == 0:
        return 0
    return (1 if numero%10 ==digito else 0) + contar_digito(numero // 10,digito)

num = int(input("Por favor ingrese un numero entero positivo: "))
dig = int(input("Por favor ingrese un digito entre 0 y 9: "))

print(f"El digito {dig} aparece {contar_digito(num,dig)} veces en el numero {num}")