"""
Un programa para almacenar información de libros
Titulo, Autor
Año, ISBN

El usuario puede:
VER, Añadir, Actualizar, Borrar y Cerrar registros

Programador: Ricardo Goti
"""
from tkinter import *
import back_end

def get_selected_row(event):
    try:
        global selected_tuple
        index=lista1.curselection()[0]    #Metodo para reconocer seleccion con el MOUSE
        selected_tuple=lista1.get(index)
        #Borramos y escribimos el contenido de todos los entry
        entry1.delete(0,END)
        entry1.insert(END,selected_tuple[1])
        entry2.delete(0,END)
        entry2.insert(END,selected_tuple[2])
        entry3.delete(0,END)
        entry3.insert(END,selected_tuple[3])
        entry4.delete(0,END)
        entry4.insert(END,selected_tuple[4])
    except IndexError:
        pass

def view_command():
    lista1.delete(0,END)
    for row in back_end.view():
        lista1.insert(END,row)

def search_command():
    lista1.delete(0,END)
    for row in back_end.search(title_text.get(), author_text.get(), year_text.get(),isbn_text.get()):
        lista1.insert(END,row)

def add_command():
    back_end.insert(title_text.get(), author_text.get(), year_text.get(),isbn_text.get())
    lista1.delete(0,END)
    lista1.insert(END,(title_text.get(), author_text.get(), year_text.get(),isbn_text.get()))

def delete_command():
    back_end.delete(selected_tuple[0])
    view_command()
    #Borramos los datos en los data entry
    entry1.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)
    entry4.delete(0,END)

def update_command():
    back_end.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(),isbn_text.get())
    view_command()
    entry1.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)
    entry4.delete(0,END)

window=Tk()
window.wm_title("LIBRERIA DEL MAL")

"""
Declaración de todos los labels del programa
"""
label1=Label(window,text="Titulo del Libro -> ")
label1.grid(row=0,column=0)
label2=Label(window,text="Autor del Libro -> ")
label2.grid(row=0,column=2)
label3=Label(window,text="Año -> ")
label3.grid(row=1,column=0)
label4=Label(window,text="ISBN -> ")
label4.grid(row=1,column=2)

#label para reacomodo!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
label5=Label(window,text="")
label5.grid(row=2,column=0)
label6=Label(window,text="")
label6.grid(row=2,column=1)
label7=Label(window,text="")
label7.grid(row=2,column=2)
label8=Label(window,text="")
label8.grid(row=2,column=3)
label9=Label(window,text="")
label9.grid(row=9,column=0)
label10=Label(window,text="")
label10.grid(row=9,column=1)
label11=Label(window,text="")
label11.grid(row=9,column=2)
label12=Label(window,text="")
label12.grid(row=9,column=3)

"""
Declaración de todos los data entry del programa
"""
title_text=StringVar()
entry1=Entry(window,textvariable=title_text)
entry1.grid(row=0,column=1)
author_text=StringVar()
entry2=Entry(window,textvariable=author_text)
entry2.grid(row=0,column=3)
year_text=StringVar()
entry3=Entry(window,textvariable=year_text)
entry3.grid(row=1,column=1)
isbn_text=StringVar()
entry4=Entry(window,textvariable=isbn_text)
entry4.grid(row=1,column=3)

#Creacion de la lista
lista1=Listbox(window, height=10, width=55)
lista1.grid(row=3, column=0, rowspan=6, columnspan=2)
#Creacion del Scrollbar
sb1=Scrollbar(window)
sb1.grid(row=3, column=2, rowspan=6)
#Configuracion de la listo junto a su Scrollbar
lista1.configure(yscrollcommand=sb1.set)
sb1.configure(command=lista1.yview)

lista1.bind('<<ListboxSelect>>',get_selected_row)
"""
Declaración de todos los botones
"""
#Declaración de los botones

button1=Button(window, text="VIEW ALL", width = 20, command=view_command)
button1.grid(row=3,column=3)
button2=Button(window, text="SEARCH ENTRY", width = 20, command=search_command)
button2.grid(row=4,column=3)
button3=Button(window, text="ADD ENTRY", width = 20, command=add_command)
button3.grid(row=5,column=3)
button4=Button(window, text="UPDATE SELECTED", width = 20, command=update_command)
button4.grid(row=6,column=3)
button5=Button(window, text="DELETE SELECTED", width = 20, command=delete_command)
button5.grid(row=7,column=3)
button6=Button(window, text="CLOSE", width = 20, command=window.destroy)
button6.grid(row=8,column=3)

window.mainloop()
