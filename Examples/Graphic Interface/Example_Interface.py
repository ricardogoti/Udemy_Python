from tkinter import *

def km_to_miles():
    t1.delete("1.0", END) #Metodo para borrar el contenido en el widget Text
    t1.insert(END,float(e1_value.get())*1.6)

window=Tk()

l1=Label(window,text="Introduce el Texto -> ")
l1.grid(row=0,column=0)

e1_value=StringVar()
e1=Entry(window, textvariable=e1_value)
e1.grid(row=0,column=1)

b1=Button(window, text="Aprietame!!!!!", command=km_to_miles)
b1.grid(row=0,column=4)




t1=Text(window, height=3, width=20)
t1.grid(row=1,column=0)

window.mainloop()

######################################
#       1 kg = 1000 grams
#       1 kg = 2.20462 pounds
#       1 kg = 35.274 ounces
###333################################
