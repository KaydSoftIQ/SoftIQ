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
#This is used for the frontend
'''
k = input("Action: ")

if k == "Age":
    i = int(input("Age: "))
else:
    i = input(":")
'''



class CollectingData:

    def collecting(k,i):
        print(test.count_data(k,i))



class DataTable:

    def __init__(self):
        self.data = {}
        

    def insert_data(self, name, **kwargs):
        self.data[name] = kwargs
        self.data[name]["Name"] = name

    def count_data(self, data, value):
        c=0

        for i in self.data:
            if self.data[i][data] == value:
                c += 1
        return c

        

test = DataTable()
test.insert_data("Joao", Age=16, HairColour="Black", Sex="Male", Role="Programmer")
test.insert_data("Oliver", Age=16, HairColour="Brown", Sex="Male", Role="Programmer")
test.insert_data("KayD", Age=19, HairColour="Black", Sex="Female", Role="Musician")
CollectingData.collecting(k,i)
#print(test.count_data("Age",16))