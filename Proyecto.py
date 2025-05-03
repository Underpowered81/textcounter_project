'''
Objetivo General
    Crear un programa capaz de leer un archivo de texto y generar tablas de estadistica.

Debe ser capaz de abrir un documento de texto llamado "TextoCompleto.txt"
    Leer el documento y extraer la informacion solicitada.
        Esta informacion seran 6 palabras (No solo texto o palabras coherentes,
          sino una linea de caracteres, siendo palabras con mayuscula distintas a
          aquellas con minuscula).

        El programa debera leer cada linea del archivo y contar cuantas veces
          se presentan las palabras indicadas por el usuario.
        
    Generar graficos con los datos sobre la informacion solicitada.

DEBE ABRIR EL DOCUMENTO EN MODO LECTURA PARA PODER LEER SU CONTENIDO



'''


#This will compare the input with any value inside 'data2.txt' and print a bool

user_input = input("Enter some text: ")

with open("data2.txt", "r") as file:
    file_content = file.read()

if user_input in file_content:      #Here there should be something that counts the times that something appears in the document
    specifiedword_number = 0
    for x in 
    
    input_1 = 1
    print(specifiedword_number)
else:
    input_1 = 0
    print("no")
file.close
pass


