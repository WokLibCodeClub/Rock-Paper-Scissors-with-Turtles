from turtle import *

screen = Screen()
screen.register_shape("yes.gif")
screen.register_shape("no.gif")

choice = ""

# Create a turtle called yes with a y image
yes = Turtle()
yes.hideturtle()
yes.shape("yes.gif")
yes.penup()
yes.goto(-100, 0)
yes.showturtle()

# Create a turtle called no with a n image
no = Turtle()
no.hideturtle()
no.shape("no.gif")
no.penup()
no.goto(100, 0)
no.showturtle()

# Define a function to happen when yes turtle is clicked
def set_yes(x, y):
    global choice
    print("y")
    # Cancel any future clicking
    yes.onclick(None)
    no.onclick(None)

# Define a function to happen when no turtle is clicked
def set_no(x, y):
    global choice
    print("n")
    # Cancel any future clicking
    yes.onclick(None)
    no.onclick(None)

'''
Set the programme waiting for the turtle to be clicked
and when it is clicked call functon recolour
'''
yes.onclick(set_yes)
no.onclick(set_no)
