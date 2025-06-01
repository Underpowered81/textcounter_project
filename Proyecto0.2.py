'''
General Objective
    Create a program that can read a text document called "TextoCompleto.txt"
    and get certain information to create graphs wwith the values

Specific Objectives
    1. Ask the user for input in which words they want to search in the document.

    2. Make the program read "TextoCompleto" = TxtCom, to get the following info:
        2.1. Get the ammount of lines present in the document and store them in a 
        variable for later use
        2.2. Get the largest ammount of times any word appear in the document and 
        store for later use
        2.3. Generate a graph that uses (0, 0) to (xvalue, yvalue), being "yvalue" 
        the ammount times a word was found in a line, and "xvalue" being the line
        that the "yvalue" was located in

        2.2. Generate a values table that prints the ammount of times the word appears 
        in the whole document, maximum and minimum ammount of times a word appears in
        a paragraph, the mean, median, and mode
            2.2.0. Example table:
            2.2.1.
            2.2.2.  ESTADISTICAS DE PALABRAS
            2.2.3.  Palabra 1: (word1)
            2.2.4.  Total de ocurrencias: (times1)
            2.2.5.  MAXIMA cantidad de occurencias:(maximum1)
            2.2.6.  MINIMA cantidad de occurencias:(minimum1)
            2.2.7.  MEDIA de occurencias:(mean1)
            2.2.8.  MEDIANA de occurencias:(median1)
            2.2.9.  MODA de occurencias:(mode1)
            2.2.10.
            2.2.11. ESTADISTICAS DE PALABRAS
            2.2.12. Palabra 2: (word2)
            2.2.13. Total de ocurrencias: (times2)
            2.2.14. MAXIMA cantidad de ocurrencias:(maximum2)
            2.2.15. MINIMA cantidad de ocurrencias:(minimum2)
            2.2.16. MEDIA de ocurrencias:(mean2)
            2.2.17. MEDIANA de occurencias:(median2)
            2.2.18. MODA de occurencias:(mode2)
            2.2.19.
            2.2.20. ESTADISTICAS DE PALABRAS
            2.2.21. Palabra 3: (word3)
            2.2.22. Total de ocurrencias: (times3)
            2.2.23. MAXIMA cantidad de occurencias:(maximum3)
            2.2.24. MINIMA cantidad de occurencias:(minimum3)
            2.2.25. MEDIA de occurencias:(mean3)
            2.2.26. MEDIANA de occurencias:(median3)
            2.2.26. MODA de occurencias:(mode3)


'''


#This will compare the input with any value inside 'data2.txt' and print a bool

user_input = input("Enter some text: ")

with open("data2.txt", "r") as file:
    file_content = file.read()

if user_input in file_content:      #Here there should be something that counts the times that something appears in the document
    specifiedword_number = 0
    for x in file_content:
        print(x)
    
    input_1 = 1
    print(specifiedword_number)
else:
    input_1 = 0
    print("no")
file.close
pass


