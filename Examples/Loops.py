def emails_func():
    emails=["me@gmail.com","you@gmail.com", "she@gmail.com", "he@hotmail"]
    for email in emails:
        if "hotmail" in email:
            print(email)

def loop_func():
    mylist=[1,2,3,4,5]
    for x in mylist:
        if x > 2:
            print(x)

def currency_converter():
    rate=float(input("Enter rate: "))
    euros=float(input("Enter euros: "))
    print(euros*rate)


##loop_func()
#Lectura de la rata y cantidad
#currency_converter()
planet = input("What planet are you from ? ")
print (planet)

#Ejemplo del uso del WHILE LOOP
password = ""
while password != "python123":
    password = input("Enter Password: ")
    if password == "python123":
        print("You are logged in !!!")
    else:
        print("Sorry, try again !!!")

#LOOP with Multiple Lines
names=["James","John","Jack"]
email_domains=["gmail","hotmail","yahoo"]
for a,b in zip(names, email_domains):
    print(a,b)
