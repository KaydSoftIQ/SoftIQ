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
#test.insert_data(n, Age=a, Haircolour=hc, Sex=s, Role=r)
#print(test.count_data("Age",16))
