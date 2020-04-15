# Step 6 - Controlling the game using just the mouse

Lots of games in Scratch involve clicking on one of the sprites. When you click on a sprite it creates what is called an *event* and this is used as a message to make something happen.

We can do the same with Python turtles.

## Making a turtle react to being clicked

Open a **new python file** and copy in this short programme to see how this works:

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
# and when it is clicked call function recolour
t.onclick(recolour)
```
>### Special Note if you are writing your code with the *Visual Studio Code* editor:
>you need to add the line ```mainloop()``` as the *last* line of this code to keep the turtle window open.

The new idea in this code is the line ```t.onclick(recolour)```. This sets the programme waiting for the turtle called ```t``` to be clicked. In fact the programme won't do anything at all until the turtle is clicked. When it *is* clicked the programme runs the function called ```recolour```. If you want to guess what happens if you click the turtle look at the code inside function ```recolour()``` and see if you can work it out.

Save the code and run it - you should see a black square in the middle of the screen. Click on it to see what happens.

### Stopping a turtle reacting to being clicked

Sometimes we need to prevent a turtle reacting to a click. To show how this works this add an extra line at the end of function ```recolour()```:
```
    t.onclick(None)
```
This line disables turtle clicking for turtle ```t```. By putting it inside the function we can ensure the turtle only reacts to a click once - because the first turtle click makes the function run, and inside the function turtle-clicking is disabled. Save the code and try it - the turtle only reacts the first time you click it - clicking again doesn't make anything happen.

## Using turtle clicking to control Rock, Paper, Scissors

We will use this idea to adapt Rock, Paper, Scissors to run using mouse clicks instead of the keyboard.

First save your Rock, Paper, Scissors Python file with a **new name**, so that you can make the changes in the new file and keep the previous version separate. 

### Make new turtles to use for choices

To run the code with mouse clicks we need *five* new turtles: three to be clicked to let the player choose rock, paper or scissors, and two more to be clicked to let the player choose "yes" or "no" for playing again. You can name them whatever you like, but I called mine ```choose_rock```, ```choose_paper```, ```choose_scissors```, ```choose_yes``` and ```choose_no```. Add one line of code to create each turtle, and make sure these lines are above the ```for``` loop which sets turtle properties.

### Get extra images

We can use hand images we already have to choose Rock, Paper or Scissors, but for asking about playing the game again we need two new images, which show the letters "y" and "n" on a white background. Get these images by clicking on this link [Extra images](extra_images.zip) and then click on the download button.

After saving this file in the project folder **_you will have to unzip it_** to make the images available to use.

After you have unzipped the file you will find two new image files in your project folder called ```yes.gif``` and ```no.gif```, so we have to make these images available to Python using the same command we used before:
```
screen.register_shape("*****")
```
The name of the image file will go in place of the asterisks, and you will need a line of code for each new image. Place the new lines together with the lines that register the other image files.

### Give the new turtles the right images

Each of the new turtles needs take the shape of one of the image files so for each new turtle add a line of code to do this. Put these lines in the **variables** section, above all the function definitions. Here is the code I used for the ```choose_rock``` turtle:
```
choose_rock.shape("you_rock.gif")
```

Add a similar line for *each of the other four* new turtles, selecting the correct image files.

### Rewrite the function ```get_choice()```

Now that we're going to choose rock, paper or scissors by clicking turtles, rather than using the keyboard, we need to completely rewrite the function ```get_choice()```. 

_*Delete*_ all the code in the definition of this function, except the first line ```def get_choice():```.

We will use the referee turtle to give the instruction to the player "Click on rock, paper or scissors:", so put these lines at the beginning of the function definition:
```
    referee.goto(-350, 300)
    referee.write("Click on rock, paper or scissors:", font = ("arial", 28, 'bold'), align = "left")
```

Save your code and run it - you should see the text across the top of the screen.

For *each* of the turtles ```choose_rock```, ```choose_paper``` and ``choose_scissors``` we need two lines of code to move the turtle to a suitable x,y location and show the turtle. Here is my code for the ```choose_rock``` turtle:
```
    choose_rock.goto(-200, 220)
    choose_rock.showturtle()
```

Save your code and run it - you should now see the rock shape underneath the text. (Don't worry if this shape lies over other text on the screen - we can fix that later.)

Now add similar lines for the ```choose_paper``` and ``choose_scissors``` turtles. Save the code and test it, changing the coordinates of the second and third turtles to make sure you can see all three, and that they are not overlapping.

For each of these three turtles we need to write code to say what will happen when we click on the turtle. As in the example above, we will do this by adding an ```onclick``` command for each turtle, which will send the code to a function when the user clicks on the turtle. Then, we need to code the three functions. Here is how I made the code for clicking on the ```choose_rock``` turtle. You need to add similar code for the ```choose_paper``` and ``choose_scissors``` turtles.
1. inside the function ```get_choice()``` add this line
```
    choose_rock.onclick(rock_click)
```
2. at the end of the section containing function definitions add a new function:
```
def rock_click(x,y):
    global your_choice
    your_choice = 0
    play_game()
```
This function will set the variable ```your_choice``` to zero when you click on Rock. It will then call the function ```play_game()``` to set the game going.

Now add two more ```onclick``` commands, for the other two turtles inside function ```get_choice()``` and code two more new functions for when you click on Paper and Scissors. Remember, in the keyboard version of the game, when you selected Paper we set the variable ```your_choice```to 1, and when you selected Scissors we set the variable ```your_choice```to 2. You need to copy the same behaviour in the mouse-control version of the game.

We need to add some code at the beginning of function ```play_game()```. This is to hide the choice turtles, and to cancel the clicking, so that if you accidentally click on one of these turtles nothing will happen.

Here is the code to add for the ```choose_rock``` turtle. Put this code immediately after the line ```global your_score, computer_score```:
```
    choose_rock.hideturtle()
    choose_rock.onclick(None)
```
Now add four more lines, two for the ```choose_paper``` turtle and two for the ```choose_scissors``` turtle, to do the same operations for these other turtles.







