from softiqbackend import*

t = turtle.Turtle()

while True:
    action = 0
    print("\n1. To enter new data", "\n2. To display the data","\n3. To exit the program")
    action = int(input("Enter a number: "))
    if action == 1:
        name = input("Name: ")
        age = input("Age: ")
        hair = input("Hair Colour: ")
        sex = input("Sex (Male/Female): ")
        role = input("Role: ")
        database.inputed_data(name, age, hair, sex, role)
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
