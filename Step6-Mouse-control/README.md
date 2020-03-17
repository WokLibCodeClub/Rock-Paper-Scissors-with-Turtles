# Step 6 - Controlling the game using just the mouse

Lots of games in Scratch involve clicking on one of the sprites. When you click on a sprite it creates what is called an *event* and this is used as a trigger to make something happen.

We can do the same with Python turtles.

Open a new python file and copy in this short programme to see how this works:

(Unfortunately this won't run on trinket because you can't resize a turtle in trinket.)
```
from turtle import *
from time import sleep

# Allows turtles to be resized
resizemode("user")

# Create a turtle called t with a square shape
t = Turtle()
t.shape("square")
# Increase the height and width by a factor 4
t.turtlesize(4,4)

# Define a function to run when the turtle is clicked
def recolour(x, y):
    t.color("red")
    sleep(0.1)
    t.color("black")

# Set the programme waiting for the turtle to be clicked
# and when it is clicked call functon recolour
t.onclick(recolour)
```

This step introduces turtle.onclick()