import time
import random
import matplotlib.pyplot as plt

# --- Algoritmos de búsqueda ---

def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif objetivo < lista[medio]:
            derecha = medio - 1
        else:
            izquierda = medio + 1
    return -1

# --- Función para medir tiempos ---

def medir_tiempo(funcion, lista, objetivo, repeticiones=3):
    total = 0
    for _ in range(repeticiones):
        inicio = time.perf_counter()
        funcion(lista, objetivo)
        fin = time.perf_counter()
        total += (fin - inicio) * 1000  # milisegundos
    return total / repeticiones

# --- Generar listas ordenadas de diferentes tamaños ---

valores_n = [100, 1000, 10000, 100000, 1000000]
listas = {n: sorted([random.randint(1, 1000000) for _ in range(n)]) for n in valores_n}
objetivo = random.randint(1, 1000000)  # Objetivo aleatorio para buscar

# --- Resultados de tiempos ---

print("n\tLineal(ms)\tBinaria(ms)")
for n in valores_n:
    lista = listas[n]
    tiempo_lineal = medir_tiempo(busqueda_lineal, lista, objetivo)
    tiempo_binaria = medir_tiempo(busqueda_binaria, lista, objetivo)
    print(f"{n}\t{tiempo_lineal:.5f}\t{tiempo_binaria:.5f}")


# Almacenar tiempos
tiempos_lineal = []
tiempos_binaria = []

# Medir tiempos
for n in valores_n:
    lista = listas[n]
    tiempo_lineal = medir_tiempo(busqueda_lineal, lista, objetivo)
    tiempo_binaria = medir_tiempo(busqueda_binaria, lista, objetivo)
    tiempos_lineal.append(tiempo_lineal)
    tiempos_binaria.append(tiempo_binaria)

# Crear gráficos
plt.figure(figsize=(10, 6))
plt.plot(valores_n, tiempos_lineal, label='Búsqueda Lineal', marker='o')
plt.plot(valores_n, tiempos_binaria, label='Búsqueda Binaria', marker='s')
plt.xscale('log')  # Escala logarítmica para el eje x
plt.yscale('log')  # Escala logarítmica para el eje y
plt.xlabel('Tamaño de la lista (n)')
plt.ylabel('Tiempo de ejecución (ms)')
plt.title('Comparación de Tiempos: Búsqueda Lineal vs Binaria')
plt.legend()
plt.grid(True, which="both", ls="--")
plt.show()


