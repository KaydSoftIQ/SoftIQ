
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