import turtle
#from softiqturtlebackend import *


ginger_hcolour_number = 0
brown_hcolour_number = 0
blond_hcolour_number = 0
black_hcolour_number = 0

gender_number = 0


class database:

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

    def inputed_data(t, n, a, h, s, r):
        print("Data Stored")

    def select_data(t, d):

        hcolour_number = 0
        gender_number = 0

        # to count the number of items in the hair colour section

        # searches each list to find if the given hair colour is present
        # if the hair colour is in the list then a count is summed to find how many of the same hair colour is in all the lists
        if d == "Ginger":
            if d == p1[2]:
                hcolour_number += 1
            if d == p2[2]:
                hcolour_number += 1
            if d == p3[2]:
                hcolour_number += 1
            if d == p4[2]:
                hcolour_number += 1
            if d == p5[2]:
                hcolour_number += 1
            if d == p6[2]:
                hcolour_number += 1
            if d == p7[2]:
                hcolour_number += 1
            if d == p8[2]:
                hcolour_number += 1
            if d == p9[2]:
                hcolour_number += 1
            if d == p10[2]:
                hcolour_number += 1
            print(hcolour_number)

        elif d == "Brown":
            if d == p1[2]:
                hcolour_number += 1
            if d == p2[2]:
                hcolour_number += 1
            if d == p3[2]:
                hcolour_number += 1
            if d == p4[2]:
                hcolour_number += 1
            if d == p5[2]:
                hcolour_number += 1
            if d == p6[2]:
                hcolour_number += 1
            if d == p7[2]:
                hcolour_number += 1
            if d == p8[2]:
                hcolour_number += 1
            if d == p9[2]:
                hcolour_number += 1
            if d == p10[2]:
                hcolour_number += 1
            print(hcolour_number)

        elif d == "Blond":
            if d == p1[2]:
                hcolour_number += 1
            if d == p2[2]:
                hcolour_number += 1
            if d == p3[2]:
                hcolour_number += 1
            if d == p4[2]:
                hcolour_number += 1
            if d == p5[2]:
                hcolour_number += 1
            if d == p6[2]:
                hcolour_number += 1
            if d == p7[2]:
                hcolour_number += 1
            if d == p8[2]:
                hcolour_number += 1
            if d == p9[2]:
                hcolour_number += 1
            if d == p10[2]:
                hcolour_number += 1
            print(hcolour_number)

        elif d == "Black":
            if d == p1[2]:
                hcolour_number += 1
            if d == p2[2]:
                hcolour_number += 1
            if d == p3[2]:
                hcolour_number += 1
            if d == p4[2]:
                hcolour_number += 1
            if d == p5[2]:
                hcolour_number += 1
            if d == p6[2]:
                hcolour_number += 1
            if d == p7[2]:
                hcolour_number += 1
            if d == p8[2]:
                hcolour_number += 1
            if d == p9[2]:
                hcolour_number += 1
            if d == p10[2]:
                hcolour_number += 1
            print(hcolour_number)
        else:
            print("That is not an option.")

        # to count the number of items in the hair colour section

        # searches each list to find out if there is a specific gender in that list
        # if there is then it will sum it up
        if d == "Female":
            if d == p1[3]:
                gender_number += 1
            if d == p2[3]:
                gender_number += 1
            if d == p3[3]:
                gender_number += 1
            if d == p4[3]:
                gender_number += 1
            if d == p5[3]:
                gender_number += 1
            if d == p6[3]:
                gender_number += 1
            if d == p7[3]:
                gender_number += 1
            if d == p8[3]:
                gender_number += 1
            if d == p9[3]:
                gender_number += 1
            if d == p10[3]:
                gender_number += 1
            print(gender_number)

        elif d == "Male":
            if d == p1[3]:
                gender_number += 1
            if d == p2[3]:
                gender_number += 1
            if d == p3[3]:
                gender_number += 1
            if d == p4[3]:
                gender_number += 1
            if d == p5[3]:
                gender_number += 1
            if d == p6[3]:
                gender_number += 1
            if d == p7[3]:
                gender_number += 1
            if d == p8[3]:
                gender_number += 1
            if d == p9[3]:
                gender_number += 1
            if d == p10[3]:
                gender_number += 1
            print(gender_number)


#     Name         Age      HC           Gender       Role
p1 = ["Sarah",     "16",    "Ginger",    "Female",    "W"]
p2 = ["Joao",      "19",    "Brown",     "Male",      "L"]
p3 = ["Oliver",    "34",    "Brown",     "Male",      "W"]
p4 = ["Dan",       "11",    "Ginger",    "Male",    "L"]
p5 = ["Luke",      "29",    "Blond",     "Male",      "L"]
p6 = ["John",      "35",    "Brown",     "Male",      "W"]
p7 = ["Sara",      "66",    "Black",     "Female",    "L"]
p8 = ["Melody",    "16",    "Black",     "Female",    "W"]
p9 = ["Brian",     "24",    "Blond",     "Male",      "W"]
p10 = ["Shaniqua", "65",    "Ginger",    "Female",    "L"]



