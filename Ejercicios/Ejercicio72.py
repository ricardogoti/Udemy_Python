import datetime

def create_file(contenido):
    with open (datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt","a+") as file:
        for indice in range(3):
            file.write(contenido[indice]+"\n") #Overwrite/create empty file with a string


def leer_archivo(indice):
    filename = "file"+str(indice)+".txt"
    with open (filename, "r") as file:
        file.seek(0)
        return file.read()

contenido =[]
for indice in range(3):
    leer_archivo(indice+1) #Almaceno el contenido de los archivos luego de leerlos
    contenido.append(leer_archivo(indice+1))

create_file(contenido)
