# Write a script that walks through a nested folder structure 
# and prints out all the Python files it can find.
# Run it in your labs folder and add formatting for nicer viewing.

import pathlib, os

path = input("Welcome! Please input a path, or leave empty to denote the current working directory: ")

while True:
    try:
        if len(path) == 0:
            path = pathlib.Path()
        else:
            path = pathlib.Path(path)
        break
    except:
        print("Sorry. That path wasn't valid. Try again.")

tabs = ""
for root, dirs, files in os.walk(path):

    print(root)
    tabs += "\t"

    for file in files:
        if file.endswith(".py"):
            print(tabs + file)
    
    tabs = tabs[:-1]

    