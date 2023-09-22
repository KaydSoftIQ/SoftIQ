'''

# Jacob's Notes -- Okay, now can we make it class based (OOP) and draw the bars to scale based on the data? An axis is also needed


# Python program to draw a turtle
import turtle

# Function that draws the turtle
def drawBar(t, height, color):

	# Get turtle t to draw one bar
	# of height
	
	# Start filling this shape
	t.fillcolor(color)
	t.begin_fill()			
	t.left(90)
	t.forward(height)
	t.write(str(height))
	t.right(90)
	t.forward(40)
	t.right(90)
	t.forward(height)
	t.left(90)
	
	# stop filling the shape
	t.end_fill()				

# Driver Code

xs = [48, 56, 45]
clrs = ["pink",  "blue", "magenta", ]
# Test
maxheight = max(xs)
numbers = len(xs)
border = 110
padding = 125

# Set up the window and its
# attributes
wn = turtle.Screen()			
wn.setworldcoordinates(0 - border, 0 - border,
					40 * numbers + border,
					maxheight + border)

# Create tess and set some attributes
tess = turtle.Turtle()		
tess.pensize(3)

for i in range(len(xs)):
	
	drawBar (tess, xs[i],
			clrs[i])

wn.exitonclick()

'''

'''
import turtle

def draw_chart(data):
    max_people = max(data.values(), default=0)
    chart_height = 300
    chart_width = 400
    bar_width = chart_width / len(data)

    #create a turtle object
    chart_turtle = turtle.Turtle()

    #Move to starting position
    chart_turtle.penup()
    chart_turtle.goto(-chart_width / 2,-chart_height / 2)
    chart_turtle.pendown()

    for key, value in data.items():
        bar_height = value(value / max_people)*chart_height
        chart_turtle.forward(bar_width)
        chart_turtle.left(90)
        chart_turtle.forward(bar_height)
        chart_turtle.left(90)
        chart_turtle.forward(bar_width)
        chart_turtle.left(90)
        chart_turtle.forward(bar_height)
        chart_turtle.left(90)
        chart_turtle.write(f'{key} - {value}', align='center')

    chart_turtle.hideturtle()
    turtle.done
        

'''

#test


'''

import turtle
import csv 



def read_data_from_csv(filename):
	data = {}
	with open(filename, 'r') as file:
		reader = csv.DictReader(file)
		for row in reader:
			data[row['Category']] = int(row['Value'])
	return data 
def draw_chart(data):
	max_value = max(data.values(), default=0)
	chart_height = 300
	chart_width = 400 
	bar_width = chart_width / len(data) 
	
turtle.speed(1)
    
for category, value in data.items():
        bar_height = (value / max_value) * chart_height
        turtle.forward(bar_width)
        turtle.left(90) 
        turtle.forward(bar_height) 
        turtle.left(90) 
        turtle.forward(bar_width) 
        turtle.left(90) 
        turtle.forward(bar_height) 
        turtle.left(90) 
        turtle.penup() 
        turtle.goto(turtle.xcor() + bar_width, 0) 
        turtle.pendown() 
        turtle.write(f'{category} - {value}', align='center') 
        turtle.hideturtle() 
        turtle.done() 
		# Example usage: Read data from "data.csv" and draw the chart data = read_data_from_csv("data.csv") draw_chart(data)

'''


import turtle
t=turtle.Turtle()

width = (25)
height = (50)

def draw_chart():
	t.left(90)
	t.forward(500)
	t.backward(500)
	t.right(90)
	t.forward(500)
	t.backward(500)
	
def first_bar():
	t.forward(50)
	t.left(90)
	t.forward(height)
	t.right(90)
	t.forward(width)
	t.right(90)
	t.forward(height)

	t.left(90)
	t.forward(50)
	t.left(90)
	t.forward(height)
	t.right(90)
	t.forward(width)
	t.right(90)
	t.forward(height)

	t.left(90)
	t.forward(50)
	t.left(90)
	t.forward(height)
	t.right(90)
	t.forward(width)
	t.right(90)
	t.forward(height)
	
t.penup()
t.goto(-200, -200)
t.pendown()


draw_chart()
first_bar()