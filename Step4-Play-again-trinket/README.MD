# Step 4 - Playing again - trinket

In this step we'll add code so the player can decide whether or not to play the game again. We'll do this just like we had the player choose which hand to play - by clicking on turtles. These will be two turtles showing the pictures of a letter y and a letter n.

First we'll set up these turtles, including writing click functions for each, then we'll write another function for controlling the game to ask whether to play again.

This section looks very similar to the instructions in Step2, where we set up the three 'choose' turtles.

## New turtles

### Make turtles for the choosing yes or no

We want the player to choose yes or no by clicking on turtles. We have to make *two* new turtles to show the options. We can call these ```yes``` and ```no```.

Underneath the lines in your code which create the 'choose' turtles add two more lines to create turtles. The first is

```python
yes = Turtle()
```

Now add the line to make the ```no``` turtle. As these turtles occur in the code before the ```for``` loop the new turtles will automatically get the same settings for penup, hide, speed.

### Define the shapes for the yes/no turtles

The image file for the ```yes``` turtle is ```'yes.gif'```. *After the code which sets the shape of the 'choose' turtles* add a line to set the shape for the ```yes``` turtle:

```python
yes.shape('yes.gif')
```

then another line to set the shape for the ```no``` turtle.

### Setting locations for the yes/no turtles

We want to send the yes and no turtles to different places on the screen, so you will have to choose x and y coordinates to put inside a ```goto()``` function.

Here are suggested coordinates for the ```yes``` turtle. Put this line after the lines which set the coordinates for the 'choose' turtles:

```python
yes.goto(-50, 130)
```

then underneath, put in a similar line with slightly different coordinates for the ```no``` turtle.

### Testing the locations

To test that we are happy with the positions of the new turtles we need to *show* them. We also need to suspend the game temporarily.

Go to the **MAIN CODE** section and put a ```#``` sign at the beginning of the line ```make_choice()```. This will turn this line into a comment, so it won't run. (We will remove this ```#``` in a bit.)

Now go back to the ```goto()``` lines for the yes/no turtles and add lines to *show* these turtles. For the ```yes``` turtle this is

```python
yes.showturtle()
```

Add the line to show the ```no``` turtle.

Click on Run and you should see your two new turtles. Adjust the x and y coordinates until the turtles are spaced nicely on the screen.

### Setting what happens when you click the yes/no turtles

In the section of the code **FUNCTIONS** we will now add two new functions. Put these after the three click functions for the 'choose' turtles. The first is

```python
def click_yes(x,y):
  global new_game
  new_game = True
  print(new_game)
```

Here we have made a new global variable called ```new_game```, which is a *Boolean* variable, meaning it can have only two values: ```True``` or ```False```. If the player clicks the ```yes``` turtle we will set this variable to ```True```. The last line in this function is just a test line, like we made before - if you click the turtle it will print 'True' in the text window, just to show it's working properly.

Write a similar function for the ```no``` turtle, except set ```play_game``` to ```False```.

We need to set Python to *listen* for clicking on these turtles, so to test this, we need to add two *temporary* lines in the **MAIN CODE** section. We will move these lines later. The first line, for the ```yes``` turtle, is:

```python
yes.onclick(click_yes)
```

Next, add the line for the ```no``` turtle.

Run the code, click on the yes and no turtles and check that it prints 'True' or 'False' correctly in the text window.

## New function

Next we'll write a function called ```play_again()``` which will control the yes and no turtles. Put this at the end of the **FUNCTIONS** section of code after the function ```make_choice()```.

In this function we first set it to use the global variable ```new_game```, then set up a Python ```if``` block to check the value of this variable.

```python
def play_again():
  global new_game
  if new_game:

  else:
```

Obviously this is not yet a complete function. If ```new_game = False``` (the player clicked 'n') the code will go to the ```else``` block, and in this case we want to terminate the game, so fill this block in first. After the word ```else:``` put these lines (indented *twice*):

```python
    screen.bye()
    exit()
```


## Undo the temporary lines of code

We put in some temporary lines of code to test the yes/no turtles and now we need to take them out.

1. In the two functions ```click_yes(x,y)``` and ```click_no(x,y)``` remove the line ```print(new_game)``` and replace it with a line which *calls* the ```play_again()``` function.

2. In the section **MAIN CODE** ***remove*** the ```#``` sign before ```make_choice()```.

[Go to Step 5 for trinket](../Step5-Keeping-score-trinket)

[Go back to previous page](../Step3-Play-the-game-trinket)
