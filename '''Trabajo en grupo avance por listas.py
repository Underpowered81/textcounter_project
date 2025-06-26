'''Trabajo en grupo

Proposito:

Algoritmo

1.abrir archivo
2.texto <-- cargar archivo de texto
3.palabras <-- pedir al usuario
4.palabras <-- leer'''

#cargamos el archivo y leemos las lineas(parrafos) del texto
Text = input("Ingrese el directorio del texto:")
with open(Text, 'r') as archivo:
    lineas = archivo.readlines()

import matplotlib.pyplot as plt
import numpy as np
import statistics as stats
#creamos una lista para las 6 palabras
print("ingrese 6 palabras: ")
palabra1 = input()
palabra2 = input()
palabra3 = input()
palabra4 = input()
palabra5 = input()
palabra6 = input()
n_lineas = [1,2,3,4]
P1 = [] 
P2 = [] 
P3 = []
P4 = []
P5 = []
P6 = []
a = 1
#recorremos las listas
for num_linea, linea in enumerate(lineas, start=1):
    if palabra1 in linea or palabra2 in linea or palabra3 in linea or palabra3 in linea or palabra4 in linea or palabra5 in linea or palabra6 in linea:
        P1.append(linea.count(palabra1))
        P2.append(linea.count(palabra2))
        P3.append(linea.count(palabra3))
        P4.append(linea.count(palabra4))
        P5.append(linea.count(palabra5))
        P6.append(linea.count(palabra6))


print(n_lineas)

print(P1, P2, P3, P4, P5, P6)
media = stats.mean(P1)
mediana = stats.median(P1)
moda = stats.mode(P1)
""
with open("Estadísticas.txt", "w",) as E:
    E.write(f"ESTADISTICAS DE PALABRAS \n Palabra 1: {palabra1} \n Total de ocurrencias: {sum(P1)} \n MAXIMA cantidad de ocurrencias: {max(P1)} \n MINIMA cantidad de ocurrencias: {min(P1)} \n Media de ocurrencias: {stats.mean(P1)} \n Mediana de ocurrencias {stats.median(P1)} \n Moda de ocurrencias:{stats.mode(P1)} \n\n ")
with open("Estadísticas.txt", "a") as E: 
    E.write(f"Palabra 2: {palabra2} \n Total de ocurrencias: {sum(P2)} \n MAXIMA cantidad de ocurrencias: {max(P2)} \n MINIMA cantidad de ocurrencias: {min(P2)} \n Media de ocurrencias: {stats.mean(P2)} \n Mediana de ocurrencias {stats.median(P2)} \n Moda de ocurrencias:{stats.mode(P2)} \n\n")
    E.write(f"Palabra 3: {palabra3} \n Total de ocurrencias: {sum(P3)} \n MAXIMA cantidad de ocurrencias: {max(P3)} \n MINIMA cantidad de ocurrencias: {min(P3)} \n Media de ocurrencias: {stats.mean(P3)} \n Mediana de ocurrencias {stats.median(P3)} \n Moda de ocurrencias:{stats.mode(P3)} \n\n")
    E.write(f"Palabra 4: {palabra4} \n Total de ocurrencias: {sum(P4)} \n MAXIMA cantidad de ocurrencias: {max(P4)} \n MINIMA cantidad de ocurrencias: {min(P4)} \n Media de ocurrencias: {stats.mean(P4)} \n Mediana de ocurrencias {stats.median(P4)} \n Moda de ocurrencias:{stats.mode(P4)} \n\n")
    E.write(f"Palabra 5: {palabra5} \n Total de ocurrencias: {sum(P5)} \n MAXIMA cantidad de ocurrencias: {max(P5)} \n MINIMA cantidad de ocurrencias: {min(P5)} \n Media de ocurrencias: {stats.mean(P5)} \n Mediana de ocurrencias {stats.median(P5)} \n Moda de ocurrencias:{stats.mode(P5)} \n\n")
    E.write(f"Palabra 6: {palabra6} \n Total de ocurrencias: {sum(P6)} \n MAXIMA cantidad de ocurrencias: {max(P6)} \n MINIMA cantidad de ocurrencias: {min(P6)} \n Media de ocurrencias: {stats.mean(P6)} \n Mediana de ocurrencias {stats.median(P6)} \n Moda de ocurrencias:{stats.mode(P6)} \n\n")
"""
P1.reverse()
print(P1)
O1 = int(P1[0])
O2 = int(P1[1])
O3 = int(P1[2])
O4 = int(P1[3])


x = np.array([n_lineas])
y = np.array([P1])
plt.plot(x,y)

plt.title(palabra1)
plt.show()
"""