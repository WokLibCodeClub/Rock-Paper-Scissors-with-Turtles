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

For this programme our turtles will not have the usual turtle shape, or any of the other available shapes, but will take their shapes from pictures of hands showing rock, paper and scissors. For this we need to get some images. You can create your own images later, if you want, but for now you can download a set of image files. 