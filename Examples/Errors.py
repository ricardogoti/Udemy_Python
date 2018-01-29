def divide(a,b):
    try:
        return a/b
#Puedes no poner el tipo de error y python manejara cualquier error pero lo recomendable es capturar el error en especifico
    except:
        return "BURRO no se puede dividir por CERO!!!!"

def useless(a,b):
    return "Mensaje innecesario"


print(divide(1,0))
print(useless(43,56))
