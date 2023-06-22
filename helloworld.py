import json

filename='userName.json'
name=''

try:
    with open(filename,'r') as r:
        name=json.load(r)
except IOError:
    print("Primer Loggin")

if name !="":
    print("welcome back, "+name+"!")
else:
    name = input("What is your name?")
    print("welcome, "+name+"!")
    try:
        with open(filename,'w') as f:
            json.dump(name,f)
    except IOError:
        print("There was a problem writing to the history file")