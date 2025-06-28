'''Trabajo en grupo
Algoritmo:
1 Importamos las librerías necesarias
2 Texto <---- perdirlo al usuario
3 Líneas <--- leer líneas en el Texto
4.Palabras <---- Pedir al usuario
4.1 for palara in líneas en el Texto then
4.1.1 Palabra_1_en_texto <---- cantidad de palabra 1 en texto 
4.1.2 Palabra_2_en_texto <----- cantidad de palabra 2 en texto 
4.1.3 Palabra_3_en_texto <---- cantidad de palabra 3 en texto
4.1.4 Palabra_4_en_texto <---- cantidad de palabra 4 en texto
4.1.5 Palabra_5_en_texto <---- cantidad de palabra 5 en texto
4.1.6 Palabra_6_en_texto <---- cantidad de palabra 6 en texto
4.1.7 número de líneas <---- número_de_linea
5 Total_de_palabras_dentro_del_texto <--- palabra_1_en_texto, palabra_2_en_texto, palabra_3_en_texto, palabra_4_en_texto, palabra_5_en_texto, palabra_6_en_texto
6 Número_más_grande <----- Máximo(Total_de_palabras_dentro_del_texto)
7 fuente_título_principal <-- (Tipo de letra, color de letra, tamaño de letra, grueso de letra)
8 fuente_título_grafica <-- (Tipo de letra, color de letra, tamaño de letra)
9 definir_figura_graficos <--- modulo matplotlib (cantidad de subplots, tamaño de la figura, establecimiento de números para las cordenadas)
9.1 ubicación grafica 1 <---- ubicación 
9.2 Subplot1 <--- (cantidad de líneas, Palabra_1_en_texto, color)
9.3 Subplit1_titulo <--- (palabra1, color, fuente_título_grafica)
9.4 ubicación grafica 2 <---- ubicación 
9.5 Subplot2 <--- (cantidad de líneas, Palabra_2_en_texto, color)
9.6 Subplit2_titulo <--- (palabra1, color, fuente_titulo_grafica)
9.7 ubicación grafica 3 <---- ubicación 
9.8 Subplot3 <--- (cantidad de líneas, Palabra_3_en_texto, color)
9.9 Subplit3_titulo <--- (palabra1, color, fuente_titulo_grafica)
9.10 ubicación grafica 4 <---- ubicación 
9.11 Subplot4 <--- (cantidad de líneas, Palabra_4_en_texto, color)
9.12 Subplit4_titulo <--- (palabra1, color, fuente_titulo_grafica)
9.13 ubicación grafica 5 <---- ubicación 
9.14 Subplot5 <--- (cantidad de líneas, Palabra_5_en_texto, color)
9.15 Subplit5_titulo <--- (palabra1, color, fuente_titulo_grafica)
9.16 ubicación grafica 6 <---- ubicación 
9.17 Subplot6 <--- (cantidad de líneas, Palabra_6_en_texto, color)
9.18 Subplit6_titulo <--- (palabra1, color, fuente_titulo_grafica)
10 print ("Desea salvar los valores estadísticos (S/N): ")
11 respuesta <--- usuario
12 if respuesta afirmativa then
12.1 Estadísticas.txt <--- crear o abrir para escribir
12.2 Estadísticas.txt <--- write ("ESTADISTICAS DE PALABRAS", estadísticas de cada palabra)
12.3 print ("El Archivo de texto Estadisticas.txt ha sido creado en la carpeta del programa.")
    print ("¡Gracias por usar este programa!")
13 else
13.1 print ("¡Gracias por usar este programa!")

)
'''

#cargamos el archivo y leemos las lineas(parrafos) del texto
#Import open file prompt
import tkinter as tk
from tkinter import filedialog as fd

#Ask user to select file to open
Text = fd.askopenfilename(title="Seleccione un archivo:",
                          filetypes=[("Archivos de texto", "*.txt")])

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
P1 = [] 
P2 = [] 
P3 = []
P4 = []
P5 = []
P6 = []
n_1 = []
p = 1
#recorremos las listas
for num_linea, linea in enumerate(lineas, start=1):
    if palabra1 in linea or palabra2 in linea or palabra3 in linea or palabra3 in linea or palabra4 in linea or palabra5 in linea or palabra6 in linea:
        P1.append(linea.count(palabra1))
        P2.append(linea.count(palabra2))
        P3.append(linea.count(palabra3))
        P4.append(linea.count(palabra4))
        P5.append(linea.count(palabra5))
        P6.append(linea.count(palabra6))
        n_1.append(p)
        p+=1
        

N_mayor = []
N_mayor.extend(P1), N_mayor.extend(P2), N_mayor.extend(P3), N_mayor.extend(P4), N_mayor.extend(P5), N_mayor.extend(P6)
Mayor = max(N_mayor)
Fuente_t = {'family':'serif','color':'grey'} 
Fuente_ax = {'family':'serif','color':'grey','size': 14} 
fig, axes = plt.subplots(2,3,figsize=(Mayor,num_linea), sharex="row", sharey=all) 
#NP1
ax = axes [0][0] 
ax.plot(n_1,P1, color="navy")
ax.set_title(palabra1,color = "navy", fontdict = Fuente_ax)
#NP2
ax = axes [0][1] 
ax.plot(n_1,P2, color="red")
ax.set_title(palabra2, color="red", fontdict = Fuente_ax)
#NP3
ax = axes [0][2] 
ax.plot(n_1,P3,  color="darkgreen")
ax.set_title(palabra3, color="darkgreen", fontdict = Fuente_ax)
#NP4
ax = axes [1][0] 
ax.plot(n_1,P4, color="cyan")
ax.set_title(palabra4, color="cyan", fontdict = Fuente_ax)
#NP5
ax = axes [1][1] 
ax.plot(n_1,P5, color="darkblue")
ax.set_title(palabra5, color="darkblue", fontdict = Fuente_ax)
#NP6
ax = axes [1][2] 
ax.plot(n_1,P6, color="magenta")
ax.set_title(palabra6, color="magenta", fontdict = Fuente_ax)
#last
plt.suptitle("OCURRENCIAS DE PALABRAS POR PÁRRAFO", fontdict = Fuente_t, fontsize= 18, fontweight = "bold")
plt.subplots_adjust(hspace=0.4, wspace=0.45)
plt.show()

afirmación = ("S", "s", "Si", "sI", "SI", "si", "Sí", "SÍ","sí", "sÍ")
print("Desea salvar los valores estadísticos (S/N): ")
ARCHIVO = input()
if ARCHIVO in afirmación:
    with open("Estadísticas.txt", "w",) as E:
        E.write(f"ESTADISTICAS DE PALABRAS \n Palabra 1: {palabra1} \n Total de ocurrencias: {sum(P1)} \n MAXIMA cantidad de ocurrencias: {max(P1)} \n MINIMA cantidad de ocurrencias: {min(P1)} \n Media de ocurrencias: {stats.mean(P1)} \n Mediana de ocurrencias {stats.median(P1)} \n Moda de ocurrencias:{stats.mode(P1)} \n\n ")
    with open("Estadísticas.txt", "a") as E: 
        E.write(f"Palabra 2: {palabra2} \n Total de ocurrencias: {sum(P2)} \n MAXIMA cantidad de ocurrencias: {max(P2)} \n MINIMA cantidad de ocurrencias: {min(P2)} \n Media de ocurrencias: {stats.mean(P2)} \n Mediana de ocurrencias {stats.median(P2)} \n Moda de ocurrencias:{stats.mode(P2)} \n\n")
        E.write(f"Palabra 3: {palabra3} \n Total de ocurrencias: {sum(P3)} \n MAXIMA cantidad de ocurrencias: {max(P3)} \n MINIMA cantidad de ocurrencias: {min(P3)} \n Media de ocurrencias: {stats.mean(P3)} \n Mediana de ocurrencias {stats.median(P3)} \n Moda de ocurrencias:{stats.mode(P3)} \n\n")
        E.write(f"Palabra 4: {palabra4} \n Total de ocurrencias: {sum(P4)} \n MAXIMA cantidad de ocurrencias: {max(P4)} \n MINIMA cantidad de ocurrencias: {min(P4)} \n Media de ocurrencias: {stats.mean(P4)} \n Mediana de ocurrencias {stats.median(P4)} \n Moda de ocurrencias:{stats.mode(P4)} \n\n")
        E.write(f"Palabra 5: {palabra5} \n Total de ocurrencias: {sum(P5)} \n MAXIMA cantidad de ocurrencias: {max(P5)} \n MINIMA cantidad de ocurrencias: {min(P5)} \n Media de ocurrencias: {stats.mean(P5)} \n Mediana de ocurrencias {stats.median(P5)} \n Moda de ocurrencias:{stats.mode(P5)} \n\n")
        E.write(f"Palabra 6: {palabra6} \n Total de ocurrencias: {sum(P6)} \n MAXIMA cantidad de ocurrencias: {max(P6)} \n MINIMA cantidad de ocurrencias: {min(P6)} \n Media de ocurrencias: {stats.mean(P6)} \n Mediana de ocurrencias {stats.median(P6)} \n Moda de ocurrencias:{stats.mode(P6)} \n\n")
    print("El Archivo de texto Estadisticas.txt a sido creado en la carpeta del programa.")
    print("¡Gracias por usar este programa!")
else:
    print("¡Gracias por usar este programa!")
