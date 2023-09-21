import turtle
from softiqbackend import*

# Test

t = turtle.Turtle()

while True:
    action = 0
    print("1. To enter new data\n", "2. To display the data\n",
          "3. To exit the program\n")
    action = int(input("Enter a number: "))
    if action == 1:
        name = input("Name: ")
        age = input("Age: ")
        hair = input("Hair Colour: ")
        sex = input("Sex: ")
        role = input("Role: ")
        database.inputed_data(t, name, age, hair, sex, role)
    elif action == 2:
        # print("Your can select from:\n", "1. Hair Colour\n", "2. Sex\n")
        # display_category = input("Category: ")
        # database.backend_drawing(t, display_category)
        display_data = input("What do you want to select? ")
        database.select_data(t, display_data)
    elif action == 3:
        break
    else:
        pass
