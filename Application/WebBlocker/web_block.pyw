import time
from datetime import datetime as dt
#host_path="hosts"
host_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com", "facebook.com"]

while True:

    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,14):
        print("Working Hours")
        with open(host_path,'r+') as file:
            content = file.read()
            print (content)
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")


    else:
        print("Hora de Webear")
        with open(host_path,'r+') as file:
            content = file.readlines()
            file.seek(0)
            file.truncate()
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)



    time.sleep(60)
