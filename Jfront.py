from softiqbackend import*
from softiqturtlebackend import *
'''

while True:
    action = 0
    print("\n1. To enter new data", "\n2. To display the data","\n3. To exit the program")
    action = int(input("Enter a number: "))
    if action == 1:
        name = input("Name: ")
        age = int(input("Age: "))
        hair = input("Hair Colour: ")
        sex = input("Sex (Male/Female): ")
        role = input("Role: ")
        database.add_data(name, age, hair, sex, role)
    elif action == 2:
        #print("\nYour can select from:", "\n1. Hair Colour", "\n2. Sex")
        # display_category = input("Category: ")
        # database.backend_drawing(t, display_category)
        display_data = input("What do you want to select? ")
        database.collect_data(display_data)
    elif action == 3:
        break
    else:
        pass

#This is used for the frontend

k = input("Action: ")

if k == "Age":
    i = int(input("Age: "))
else:
    i = input(":")
'''

while True:
    #Full stack - there is class missing in the turtle back-end,
    action = 0
    print("\n 1) To enter data. \n 2) To display data. \n 3) Exit")
    action = int(input("Enter a number: "))

    if action == 1:
        print("Enter Data")
    elif action== 2:
        # this is the action where the data should be displayed 
        # Turtle shouldn't start before the action
        print("Display Data")


    elif action== 3:
        # DON'T Edit this action
        break
    else:
        pass

    

        

