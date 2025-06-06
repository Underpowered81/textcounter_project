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
import matplotlib.pyplot as plt
import numpy as np
#creamos una lista para las 6 palabras
print("ingrese 6 palabras: ")
palabra1 = input()
palabra2 = input()
palabra3 = input()
palabra4 = input()
palabra5 = input()
palabra6 = input()
n_linea = []
n_lineas = []
P1 = [] 
P2 = [] 
P3 = []
P4 = []
P5 = []
P6 = []
#recorremos las listas
for num_linea, linea in enumerate(lineas, start=1):
    if palabra1 in linea or palabra2 in Text or palabra3 in Text or palabra3 in Text or palabra4 in Text or palabra5 in Text or palabra6 in Text:
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
        n_lineas = str(num_linea)

        

print(n_lineas)
print(P1, P2, P3, P4, P5, P6)
n1 = P1[0]
n2 = P1[-1]
line1 = n_lineas[0]
print(n1)

x = np.array([0 , n_lineas])
y = np.array([n2, n1])
plt.plot(x,y)
plt.title(palabra1)
plt.show()