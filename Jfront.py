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
'''

while True:
    print("\n1. To enter new data")
    print("2. To display the data")
    print("3. To exit the program")

    action = input("Enter a number: ")

    if action == '1':
        name = input("Name: ")
        age = input("Age: ")
        hair = input("Hair Colour: ")
        sex = input("Sex (Male/Female): ")
        role = input("Role: ")
        

    elif action == '2':
        
        t = turtle.Turtle()

        display_data = input("What do you want to select? ")
        t.bye()

    elif action == '3':
        break