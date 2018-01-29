
import datetime

#Funcion que lee fruits.txt e imprime articulos y largo de cada uno
def fruits_func():
    archivo=open("fruits.txt","r")
    archivotemp = archivo.readlines()
    archivo.close()
    print(archivotemp)
    archivotemp = [i.rstrip("\n") for i in archivotemp]
    print (archivotemp)
    for x in archivotemp:
        print(len(x))

#Ejemplo del uso de with para leer archivo sin necesidad de cerrar los mismos
def with_func():
    with open("example.txt","a+") as file:
        file.seek(0)
        content=file.read()
        file.write("\nLine 7")



def c_to_f(c):
    if c< -273.15:
        return
        #return "That temperature doesn't make sense!"
    else:
        f=c*9/5+32
        return f

#Funcion que crea un archivo con nombre de la fecha actual del computador
def create_file():
    filename=datetime.datetime.now()
    with open (filename.strftime("%Y-%m-%d-%H-%M")+".txt","w") as file:
        file.write("") #Overwrite/create empty file with a string

def temperatures_func():
    for t in temperatures:
        temperatures=[10,-20,-289,100]
        text_temp = (c_to_f(t))
        if text_temp != None:
            with open("Lecture_66.txt","a+") as file:
                file.write(str(text_temp)+"\n")


create_file()
#################################################################
#Ejemplo de como trabajar un txt file
#fruits_func()
#################################################################

#Llamada de la funcion con el WITH statement para manejo de archivos
#with_func()
