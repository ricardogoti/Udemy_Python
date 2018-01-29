import json
from difflib import get_close_matches

#carga la data del archivo json a una variable tipo dict
data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
#get_close_matches helps to get similar matches on anything
    if len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead ? Type Y if Yes, or N if No: " % get_close_matches(word, data.keys())[0])
        if yn.lower()== "y":
            return  data[get_close_matches(word, data.keys())[0]]
        elif yn.lower() =="n":
            return "The word doesn't exist. Please double check it."
        else:
            return "The options are Y/N idiot!!!!!"
    else:
        return "The word doesn't exist. Please double check it."

output = translate(input("Enter Word: "))
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
