# Step 2 - Playing the game

In this step we will write the code for selecting which shape you want to play out of Rock, Paper or Scissors, and for the computer to select one of these shapes at random. We will then show the two shapes together and try and work out who won.

Before we proceed it's a good idea to delete some of the code from the previous step as we will be re-writing those lines:

**_DELETE THESE LINES_**

* the two lines where you set the turtle for your hand to have the shape "you_rock.gif" and the computer turtle to have the shape "computer_scissors.gif";
* the two lines which end ```****.showturtle()```

### Make lists

This project will use Python *lists* in several places. The first two lists we need are for the image files which *you* and the *computer* will use in the game. Make a list for the computer's image files like this:
```
computer_hands = ["computer_rock.gif", "computer_paper.gif", "computer_scissors.gif"]
```

Then add a line to make a similar list for the shapes for *your* hand. Watch out! The order of the shapes is important, so make sure you have the Rock, Paper and Scissors images in that order.

## Define a function for playing the game

Most Python code makes a lot of use of **functions**, so for this project we will put most of the code inside functions. 

Here is the code for defining a function for playing the game. Place this line after the code which defines the turtles:
```
def play_game():
```

This function is called ```play_game()``` but you can use a different name if you like.

All the code which is part of the function **_MUST BE INDENTED_**.

### Make your choice

In the text-only version of the game you make a choice of Rock, Paper or Scissors using the Python ```input()``` statement. For the turtle version this would mean having to switch to the Python shell window to make the choice, then switch back to the turtle window to play the game. For the turtle version we can use the turtle function ```screen.textinput()```.

### Have the computer make a choice

### Show the choices

### Who won?



[Go to Step 3 - Adding some background information](../Step3-Adding-background)
