'''Trabajo en grupo

Proposito:

Algoritmo

1.abrir archivo
2.texto <-- cargar archivo de texto
3.palabras <-- pedir al usuario
4.palabras <-- leer'''

#cargamos el archivo y leemos las lineas(parrafos) del texto
Text = input()
with open(Text, 'r') as archivo:
    lineas = archivo.readlines()
#creamos una lista para las 6 palabras
print("ingrese 6 palabras: ")
palabra1 = input()
palabra2 = input()
palabra3 = input()
palabra4 = input()
palabra5 = input()
palabra6 = input()
n_linea = []
P1 = [] 
P2 = [] 
P3 = []
P4 = []
P5 = []
P6 = []

#recorremos las listas
for num_linea, linea in enumerate(lineas, start=1):
    if palabra1 in Text or palabra2 in Text or palabra3 in Text or palabra3 in Text or palabra4 in Text or palabra5 in Text or palabra6 in Text:
        nums1 = linea.count(palabra1)
        P1.append(nums1)
        nums2 = linea.count(palabra2)
        P2.append(nums2)
        nums3 = linea.count(palabra3)
        P3.append(nums3)
        nums4 = linea.count(palabra4)
        P4.append(nums4)
        nums5 = linea.count(palabra5)
        P5.append(nums5)
        nums6 = linea.count(palabra6)
        P6.append(nums6)

print(P1, P2, P3, P4, P5, P6)


"""
a, b, c, d, e, f = conteos
fix, axs = plt.subplots (sharex = num_linea , sharey = conteos)
import matplotlib.pyplot as plt
import numpy as np


x = np.array(num_linea)
y = np.array(a)

plt.plot(x,y)
plt.title(a)
plt.show"""