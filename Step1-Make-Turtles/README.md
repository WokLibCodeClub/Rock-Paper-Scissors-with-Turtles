# Step 1 - Make the Turtles

Actually, the first step is to make a new folder for your code. You could call it *animated-rps*. Then, inside your new folder, make a new Python file. You can call it what you like, but *animated-rps.py* is one suggestion.

The first lines of code in your new Python file will be to ```import``` the Python modules you will need for this project. So at the beginning of your code type:
```
from turtle import *
from random import randint
from time import sleep
from sys import exit
```
We need the ```turtle``` module because we are using turtles, we need the ```randint()``` function from the ```random``` module to generate random numbers, we need the ```sleep()``` function from the ```time``` module to pause the programme to build up the tension, and we need the ```exit()``` function from the ```sys``` module to close the turtle window when we stop playing the game.

The next line is a Turtle command to assign the Turtle screen to a variable called ```screen```. This is so we can give commands to the screen.
```
screen = Screen()
```

For this programme our turtles will not have the usual turtle shape, or any of the other available shapes, but will take their shapes from pictures of hands showing rock, paper and scissors. For this we need to get some images. You can create your own images later if you want, but for now you can download a set of prepared image files by clicking on this link 

[images.zip](images.zip)

then clicking on the button labelled *Download*. Save the zip file in your project folder, then double click on it to open it up. Extract all the image files to your project folder. You should now have six *gif* image files in the project folder.

To use these pictures for turtles we need to "register" the image files with the turtle Screen. Here is the Python code to do this for the first image:
```
screen.register_shape("computer_paper.gif")
```

now add five more similar lines to register the five other images.

### Making some Python *lists*

If you look at the six images you will see that the three that have filenames beginning with "you" show a hand coming from the left, and the three that have filenames beginning with "computer" show a hand coming from the right.