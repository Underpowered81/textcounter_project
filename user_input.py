#This document has inside my life's work, and by that I mean my first interface, it gets the user's input in 6 different boxes for them to input their words to use in the rest of the project
def user_input(uinput):
    #Tkinter foundation
    import tkinter as tk
    from tkinter import Label
    from tkinter import Entry
    from tkinter import Button
    root = tk.Tk()
    root.title("Ingrese las palabras deseadas")

    #List of the words
    palabra_1 = "Palabra 1"
    palabra_2 = "Palabra 2"
    palabra_3 = "Palabra 3"
    palabra_4 = "Palabra 4"
    palabra_5 = "Palabra 5"
    palabra_6 = "Palabra 6"
    word_list = ["none", "none", "none", "none", "none", "none"]

    #This is the main UI order
    blank_1 = Label(root, text="          ").grid(column=1, row=4)

    word_1 = Label(root, text=palabra_1).grid(column=0, row=0)
    entry_1 = Entry(root, width=34)
    entry_1.grid(column=0, row=1)

    word_2 = Label(root, text=palabra_2).grid(column=1, row=0)
    entry_2 = Entry(root, width=34)
    entry_2.grid(column=1, row=1)

    word_3 = Label(root, text=palabra_3).grid(column=2, row=0)
    entry_3 = Entry(root, width=34)
    entry_3.grid(column=2, row=1)

    word_4 = Label(root, text=palabra_4).grid(column=0, row=3)
    entry_4 = Entry(root, width=34)
    entry_4.grid(column=0, row=4)

    word_5 = Label(root, text=palabra_5).grid(column=1, row=3)
    entry_5 = Entry(root, width=34)
    entry_5.grid(column=1, row=4)

    word_6 = Label(root, text=palabra_6).grid(column=2, row=3)
    entry_6 = Entry(root, width=34)
    entry_6.grid(column=2, row=4)

    #Function click1 for the button1
    def click1():
        palabra_1 = entry_1.get()
        palabra_2 = entry_2.get()
        palabra_3 = entry_3.get()
        palabra_4 = entry_4.get()
        palabra_5 = entry_5.get()
        palabra_6 = entry_6.get()
        word_list[0] = palabra_1
        word_list[1] = palabra_2
        word_list[2] = palabra_3
        word_list[3] = palabra_4
        word_list[4] = palabra_5
        word_list[5] = palabra_6
        if palabra_1 == '' or palabra_2 == '' or palabra_3 == '' or palabra_4 == '' or palabra_5 == '' or palabra_6 == '':
            blank_3 = Label(root, text="Error: Carácteres inválidos o ausentes", fg=("red"))
            blank_3.grid(column=1, row=5)
        else:
            root.destroy()
            return word_list

        
    #Button positioning
    blank_1 = Label(root, text="          ").grid(column=1, row=5)
    button1 = Button(root, text="Enter", command=click1).grid(column=1, row=6)
    blank_2 = Label(root, text="          ").grid(column=1, row=7)

    #This thing so that the tkinter stuff actually loads
    root.mainloop()