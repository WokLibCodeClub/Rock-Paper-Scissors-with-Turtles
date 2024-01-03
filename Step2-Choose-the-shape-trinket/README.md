# Step 2 - Choosing the shape - trinket

In this step we will write the code to let you select which shape you want to play out of Rock, Paper or Scissors. In the step after this we will have the computer select one of these shapes at random, and then show the two shapes together to see who won.

## New variables

### Make lists

This project will use Python *lists* in several places. The first two lists we need are for the image files which *you - the player* and the *computer* will use in the game.

Add these two lists *after* the ```for``` loop, but make sure you *don't* indent the lines.

Make a list for the player's image files like this:

```python
player_hands = ["left_rock.gif", "left_paper.gif", "left_scissors.gif"]
```

It is important you have the list items in this order.

Then add a line to make a similar list, called ```computer_hands```, for the shapes for *the computer's* hand. For the computer you will use the images showing a *right* hand instead of a left hand. Again, make sure the list has the images in the order Rock, Paper, Scissors.

### Make a global variable

We are going to need a variable to store the choice of Rock, Paper or Scissors that you make for the game. As this variable will be used at different places in the game we need to create it at the top of the code, which will make it a *global* variable - meaning that it can be used everywhere in the project.

Add this line of code underneath the code for making the lists:

```python
player_choice = -1
```

The global variable is called ```player_choice``` and we have set its value to -1. By setting the value to a number we are telling Python that this is a *numerical* variable. The value will be changed later.

## New turtles

### Make turtles for the player's choice

We want the player to choose which hand to play by clicking on a turtle - so we need to make *three* new turtles to show the options. We can call these ```choose_rock```, ```choose_paper``` and ```choose_scissors```.

Underneath the lines which create the turtles for the player and the computer add three more lines to create turtles. The first is

```python
choose_rock = Turtle()
```

Now add the other two lines following the same pattern.

We've been clever here: because we've made these turtles *before* the ```for``` loop the new turtles will automatically get the same settings for penup, hide, speed etc without having to write any more code.

### Define the hand shapes for the new turtles

Not surprisingly we want the ```choose_rock``` turtle to have the shape ```'left_rock.gif'```. We could use the name of the image file in brackets to do this but a neater way is to make use of one of the lists we have just made.

The list called ```player_hands``` contains the three left-hand image files, and the left-rock image is the *first* item in the list. So we could point to this image file using ```player_hands[0]```.

Underneath the line to set the ```player_choice``` variable add this line:

```python
choose_rock.shape(player_hands[0])
```

then add similar lines for the ```choose_paper``` and ```choose_scissors``` turtles to set their shapes to the correct images.

### Setting locations for the choice turtles

We want to send the three choice turtles to different places on the screen so we can see them all at the same time. We do this with the turtle ```goto()``` method. Try this line for the ```choose_rock``` turtle. Put this *after* the three lines which set the shapes for the turtles:

```python
choose_rock.goto(-120, 100)
```

then add coordinates for the other two choice turtles which will space them across the screen. Keep the y coordinate the same for each, but vary the x coordinates.

To test out our choice of coordinates we need to show these three turtles, so add three more lines of code. The first is

```python
choose_rock.showturtle()
```

now add similar lines for the other two turtles.

Run the code and you should see your three choice turtles. Adjust your x and y coordinates if you want.

## Clicking on the "choose" turtles

In Scratch we often use a "when this sprite clicked" block to make something happen when the sprite is clicked.

We can do the same with Python turtles.

### Defining functions for clicking

If you wanted to be able to click on a turtle called ```t```, for example, you would add a line of code like this:

```python
t.onclick(click_function_for_turtle_t)
```

This ensures that when turtle ```t``` is clicked Python *calls* the function which is named inside the brackets, and in this function we can define exactly what we want to happen when the turtle is clicked.

Sometimes we want to make sure the turtle *doesn't* react to being clicked. To do this we put in a line of code:

```python
t.onclick(None)
```

which cancels the clicking function.

### Clicking the "choose" turtles in Rock, Paper, Scissors

We have just made and displayed three turtles so the player can choose which hand to play, so we need to set up ```onclick()``` functions for each of them.

Put this line at the end of the code to specify a function to run if the rock turtle is clicked:

```python
choose_rock.onclick(click_rock)
```

then add similar lines for the other two "choose" turtles.

### Defining the click function for Rock

In the line of code above we have stated that we want to run a function called ```click_rock``` if the ```choose_rock``` turtle is clicked. Now we have to write that function. Define the function after the three lines which *show* the "choose" turtles.

```python
def click_rock(x,y):
```

When you click on a Python turtle Python makes a note of the exact x and y position of your mouse. Although we don't need to use these values we have to include x and y as *parameters* in the function definition - which is why we have put ```x,y``` inside the brackets.

The main purpose of the function will be to set a value for the variable ```player_choice```. If the player chooses "Rock" we will set this variable to ```0```, for Paper we will set it to ```1``` and for Scissors we will set it to ```2```. Remember that ```player_choice``` is a *global variable* so to make sure we set the value correctly the first line in our ```click_rock(x,y)``` function has to be (indented)

```python
  global player_choice
```

Now we set the value for ```player_choice``` (indented):

```python
  player_choice = 0
```

Then, just to check that we've set the value correctly we will ```print``` the value:

```python
  print(player_choice)
```

(We will comment out the print lines later as we don't need them for the game.)

That's all we want for the ```click_rock(x,y)``` function. Now write two more functions, following a similar pattern, for ```click_paper(x,y)``` and ```click_scissors(x,y)```.

Run the code and click on one of the "choose" turtles. Hopefully whenever you click the value of ```player_choice``` will appear in the Result window: 0 if you click Rock, 1 if you click Paper and 2 if you click Scissors.

### Have the computer make a choice

We don't need to ask the computer what shape to choose - we will use a random number for this. We will put the computer choice in a variable called ```computer_choice``` and select the value using the ```randint()``` function.

Add this as the first line of the function and *indent it* because it is inside the function. This line will take a whole number from 0 to 2 at random and put the value in the variable ```computer_choice```:
```
    computer_choice = randint(0, 2)
```

### Show the choices

Now we need to assign the correct image files to the turtles for your hand and the computer's hand. This is where we will use the image lists we made earlier.

Remember, in a Python list the first item is item 0, so if I had a list of, say, fruits like this:
```
my_fruits = ["banana", "cherry", "orange", "strawberry"]
```
and I wanted to do something with the item "orange" I would refer to this as ```my_fruits[2]```.

### *This is an example list. Don't copy it into your code!!!*

We want to use the lists of images. So if your choice was rock, the variable ```your_choice``` would be set to 0, and we would set the image for your hand to be item 0 of the list of your hand images. If ```your_choice``` is set to 1, then we want item 1 from the image list, and so on. Add this line, *indented* to the end of the function:
```
    ****.shape(your_hands[your_choice])
```
In place of the stars put the name of the turtle you are using for your hand.
Now add another, similar line to set the shape for the computer's hand. You need to get the image name from the other list, and you need to use the variable for the computer's choice, and the name of the turtle you are using for the computer's hand.

Now we've set the turtles to have the right hand shapes we can show the turtles, so **add two lines**, one for each turtle, to show the turtles. Don't forget to indent these lines as they are part of the function.

When you write functions they won't do anything until the functions are *called*. We often do this in the "main" part of the programme, **_which is NOT indented_**. Add this line to call the function get_choice(), at the very end of the code, not indented:
```
get_choice()
```
Now we need to call function ```play_game()```. We could put this at the end, after calling ```get_choice``` but because we always want to run this function after ```get_choice``` a better place is to call it at the end of ```get_choice```. It is very common in Python to have a function calling another function. As the last line of function ```get_choice```, indented, add this:
```
    play_game()
```

Save your code and run it.

Your code should put up a text box to ask you to choose "r", "p" or "s", then show both hands - yours and the computer's. Did you win?

Before we go further there's one little issue we need to tidy up. Good coders always have to assume that the users of their code might make a mistake. So what would happen if someone using your brilliant game accidentally typed in a choice which wasn't "r", "p" or "s"? We'll sort that out on the [next page](README2.md).



