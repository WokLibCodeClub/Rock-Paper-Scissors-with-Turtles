from turtle import *

# Allows turtles to be resized
resizemode("user")

# Create a turtle called t with a square shape
t = Turtle()
t.shape("square")
# Increase the height and width by a factor 4
t.turtlesize(4,4)

# Define a function to happen when the turtle is clicked
def recolour(x, y):
    t.color("red")
    # Cancel any future clicking
    t.onclick(None)

'''
Set the programme waiting for the turtle to be clicked
and when it is clicked call functon recolour
'''
t.onclick(recolour)
