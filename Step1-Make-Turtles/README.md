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

The next line is a Turtle command to assign the Turtle screen to a variable called ```screen```. This is so we can give commands to the screen. The second line sets the size for the turtle screen of 800 pixels across and 700 pixels high.
```
screen = Screen()
setup(800,700)
```

For this programme our turtles will not have the usual turtle shape, or any of the other available shapes, but will take their shapes from pictures of hands showing rock, paper and scissors. For this we need to get some images. You can create your own images later if you want, but for now you can download a set of prepared image files by clicking on this link 

[images.zip](images.zip)

then clicking on the button labelled *Download*. Save the zip file in your project folder, then use the **BACK** button on your browser to get back to this page.

Now, double click on the downloaded zip file to open it up. Extract all the image files to your project folder. You should now have six *gif* image files in the project folder.

To use these pictures for turtles we need to "register" the image files with the turtle Screen. Here is the Python code to do this for the first image:
```
screen.register_shape("computer_paper.gif")
```

now add five more similar lines to register the five other images.

### Making turtles for your hand and the computer's

We will make two turtles, one to show **_your_** hand for rock, paper or scissors, and one to show the computer's. We could call these turtles ```you``` and ```computer``` but you can choose any names you like.

We will create both turtles with **two** statements like this:
```
**** = Turtle()
```
where you put the turtle names instead of the stars.

We don't want to see the turtles yet, so for both turtles add the line
```
****.hideturtle()
``` 
(again, put the turtle names instead of the stars).

We also don't want to see a line drawn when we move the turtle, so add two more lines like this:
```
****.penup()
```

To test our turtles let's try out some of the image files. Let's set *your* hand to show a rock shape. Add the line
```
****.shape("you_rock.gif")
```
(put the name of the turtle for your hand in place of the stars). Now let's set the *computer's* hand to show the scissors shape:
```
****.shape("computer_scissors.gif")
```

If you look at the six images you will see that the three that have filenames beginning with "you" show a hand coming from the left, and the three that have filenames beginning with "computer" show a hand coming from the right. You should be able to work out that we want to put the "you" turtle somewhere left of the centre of the screen and the "computer" turtle somewhere to the right of the centre.

Add these lines for **each** turtle, using the appropriate turtle name instead of the stars:
```
****.goto(?,?)
****.showturtle()
```
What do you put in place of the question marks? These will be x and y coordinates for the position where the turtle will appear.  

To help you choose suitable coordinates here is a picture showing how the coordinates look on a turtle window of the size we have set:

![Example coordinates](screen_grid.png "Example coordinates") 

Once you have selected your coordinates save your code and run it. Then adjust the coordinates until the positions of the turtles looks good.

>### Special Note if you are writing your code with the *Visual Studio Code* editor:
>
>With Visual Studio Code you will find that the Turtle window opens and closes again immediately, so you don't have a chance to see what is in the window. To stop this happening you need to add a line at the *bottom* of your code which says
>```
>mainloop()
>```
>This will keep the turtle window open. Make sure this line is always the *last* line in your code - don't put any lines of code after this.
>
>If you are using the IDLE editor _*YOU DO NOT NEED THIS LINE OF CODE*_.

Now we're ready to start coding the game.

[Go to Step 2 - Playing the game](../Step2-Play-the-game)