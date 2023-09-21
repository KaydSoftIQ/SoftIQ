#from softiqturtlebackend import *


ginger_hcolour_number = 0
brown_hcolour_number = 0
blond_hcolour_number = 0
black_hcolour_number = 0

gender_number = 0


class database:

    def __init__(self):
        self.data = []

    """ 
    def backend_drawing(t, dc):
        TurtleDrawing.graph(t)

        if dc == "Hair Colour":
            t.forward(50)
            t.left(90)
            t.forward(ginger_hcolour_number)
            print("Success")
        else:
            print("Not a valid category.")
    """

    def add_data(self, n, a, h, s, r):
        # [name 0, age 1, hair 2, sex 3, role 4]
        self.data.append([n, a, h, s, r])

    def select_data(self, t):
        o = []
        if t == "name":
            for i in self.data:
                o.append(i[0])
        elif t == "age":
            for i in self.data:
                o.append(i[1])
        elif t == "hair":
            for i in self.data:
                o.append(i[2])
        elif t == "sex":
            for i in self.data:
                o.append(i[3])
        elif t == "role":
            for i in self.data:
                o.append(i[4])
        
        return o
    


    def collect_data(display_data):
        if display_data == "name":
            print(test.select_data("name"))
        elif display_data == "age":
            print(test.select_data("age"))
        elif display_data == "hair":
            print(test.select_data("hair"))
        elif display_data == "sex":
            print(test.select_data("sex"))
        elif display_data == "role":
            print(test.select_data("role"))
    




test = database()
test.add_data("Oliver",16,"Brown","Male","Programmer")
test.add_data("Joao",16,"Brown","Male","Programmer")
       
