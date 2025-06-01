'''Trabajo en grupo

Proposito:

Algoritmo

1.abrir archivo
2.texto <-- cargar archivo de texto
3.palabras <-- pedir al usuario
4.palabras <-- leer'''

#cargamos el archivo y leemos las lineas(parrafos) del texto
with open(r"c:\Users\azend\Downloads\queso.txt", 'r') as archivo:
    lineas = archivo.readlines()
#creamos una lista para las 6 palabras
print("ingrese 6 palabras: ")

palabras = []

for i in range(6):
    palabra = input(f"Palabra {i + 1}: ")
    palabras.append(palabra)
#creamos una lista para guardar los conteos por linea
conteos_por_linea = []

#recorremos las listas
for num_linea, linea in enumerate(lineas, start=1):
    # Creamos un diccionario
    conteos = {}
    for palabra in palabras:
        conteos[palabra] = linea.count(palabra)
    conteos_por_linea.append(conteos)
    
    # Mostrar resultados por línea
    print("Línea", num_linea, conteos)