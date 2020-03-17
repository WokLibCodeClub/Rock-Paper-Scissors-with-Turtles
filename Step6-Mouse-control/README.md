# Step 6 - Controlling the game using just the mouse

Lots of games in Scratch involve clicking on one of the sprites. When you click on a sprite it creates what is called an *event* and this is used as a trigger to make something happen.

We can do the same with Python turtles.

### Making a turtle react to being clicked

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
The new idea in this code is the line ```t.onclick(recolour)```. This sets the programme waiting for the turtle called ```t``` to be clicked. In fact the programme won't do anything at all until the turtle is clicked. When it *is* clicked the programme runs the function called ```recolour```. If you want to know what happens if you click the turtle look at the code inside function ```recolour()``` and see if you can work it out.

Save the code and run it - you should see a black square in the middle of the screen. Click on it to see what happens.

### Stopping a turtle reacting to being clicked

Sometimes we need to prevent a turtle reacting to a click. To show how this works this add an extra line at the end of function ```recolour()```:
```
    t.onclick(None)
```
This line disables turtle clicking for turtle ```t```. By putting it inside the function we can ensure the turtle only reacts to a click once - because the first turtle click makes the function run, and inside the function turtle-clicking is disabled. Save the code and try it - the turtle only reacts the first time you click it - clicking again doesn't make anything happen.

### Using turtle clicking to control Rock, Paper, Scissors

We will use this idea to adapt Rock, Paper, Scissors to run using mouse clicks instead of the keyboard.

First save your Rock, Paper, Scissors Python file with a **new name**, so that you can make the changes in the new file and keep the previous version separate. 

To run the code with mouse clicks we need *five* new turtles: three to be clicked to let the player choose rock, paper or scissors, and two more to be clicked to let the player choose "yes" or "no" for playing again. You can name them whatever you like, but I called mine ```choose_rock```, ```choose_paper```, ```choose_scissors```, ```choose_yes``` and ```choose_no```.




