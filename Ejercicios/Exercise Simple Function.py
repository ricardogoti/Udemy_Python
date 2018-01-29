#Exercise Fahrenheit is F = C × 9/5 + 32
def fahrenheit(celsius):
    if celsius < -273.15:
        print("Theres no way that could be the temperature")
    else:
        print (celsius*(9/5)+32)

#Exercise Get the len of any string
def lenfunc(string):
    print(len(string))

#Exercise Complex Functions with Conditions
def string_length(mystring):
    if type(mystring) == int:
        print("Sorry integers don't have length")
    elif type(mystring) == float:
        print("Sorry floats don't have length")
    else:
        print(len(mystring))


"""
Main Programmmm

"""
#fahrenheit(int(input("Introduzca su medida en Celcios -> ")))
#lenfunc(input("Introduzca una cadena -> "))
#string_length(1)

temperatures=[10,-20,-289,100]
for x in temperatures:
    fahrenheit(x)
