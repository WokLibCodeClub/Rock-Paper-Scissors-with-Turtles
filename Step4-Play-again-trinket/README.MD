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

### Testing the locations - adding temporary code

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
  print("Clicked y")
```

If the player clicks the ```yes``` turtle we will run this function and it will print '**Clicked y**' in the text window. This will show it's working properly. We will adjust the function to do something more useful later.

Write a similar function for the ```no``` turtle, except set it to print **Clicked n**.

We need to set Python to *listen* for clicking on these turtles, so to test this, we need to add two *temporary* lines in the **MAIN CODE** section. We will remove these lines later. The first line, for the ```yes``` turtle, is:

```python
yes.onclick(click_yes)
```

Next, add the line for the ```no``` turtle.

Run the code, click on the yes and no turtles and check that it prints 'Clicked y' or 'Clicked n' correctly in the text window.

### Undo the temporary lines of code

We put in some temporary lines of code to test the yes/no turtles and now we need to take them out before we add more code.

1. In the section **VARIABLES** find the two lines you added to *show* the ```yes``` and ```no``` turtles and  ***remove*** these lines.

2. In the section **MAIN CODE** ***remove*** the ```#``` sign before ```make_choice()```.

3. In the section **MAIN CODE** ***remove*** the two lines which set ```onclick()``` functions for the ```yes``` and ```no``` turtles.

We're now ready to start writing a new function.

## New function

Next we'll write a function called ```play_again()``` which will control the yes and no turtles and the flow of the whole game.

This function will run at the end of the game and it will do the following tasks:

- at the end of the game the player and computer turtles will still be showing on the screen, so the new function will *hide* these turtles and clear the labels for You and Computer

- next, the function will display the ```yes``` and ```no``` turtles with some text asking whether to play again, and also set these turtles to be ready for clicking

  - if the player clicks the ```no``` turtle the game will close

  - if the player clicks the ```yes``` turtle we want to clear the screen and restart the game.

In fact we won't put the code for these last two tasks in the new function - instead, we'll add code to our two existing functions ```click_yes(x,y)``` and ```click_no(x,y)``` for this.

### Defining the function

We'll put our new function at the end of the **FUNCTIONS** section of code after the function ```make_choice()```.

Put in the line to start the definition of a function called ```play_again```. Can you remember how you start the definition of a function?

<details><summary>Hint</summary>

```python
def play_again():
```

Don't forget the brackets or the colon!

</details>

<p>

### Calling the new function

Although we haven't finished writing the new function we can set up the code to call the function now. We want this function to run at the end of the game, which means at the end of the ```play_game()``` function.

Once the game is finished you might want to pause for a couple of seconds before asking whether to play again. So add two lines at the end of function ```play_game()```:

```python
  sleep(?)
  play_again()
```

Fill in a number instead of the question mark to set how many seconds the game pauses before running the function.

The first task in new our function task list was to clear the labelling and hide the ```player``` and ```computer``` turtles:

```python
  label.clear()
  player.hideturtle()
  ```

Now add the line to hide the ```computer``` turtle.

Next we want to *show* the ```yes``` and ```no``` turtles and write some text of explanation. Here is some suggested code:

```python
  label.color('black')
  label.goto(-210, 160)
  label.write('Play again? (click y or n)', font = ("arial", 14, 'bold'), align = "left")
  yes.showturtle()
  no.showturtle()
```

You can change the location of the text and the font, and the wording, if you want.

Finally we want to set these two turtles up to be clickable. For this we add in the same two lines we previously put in the MAIN CODE as temporary lines. Here is the line for the ```yes``` turtle:

```python
  yes.onclick(click_yes)
```

Now add the line for the ```no``` turtle.

### Test the code

You should now be able to Run the code. It will start by running a game of Rock-paper-scissors, then at the end it will clear the screen and display the ```yes``` and ```no``` turtles with some text.

Click on one of these and, if it's working properly, it should write 'Clicked y' or 'Clicked n' in the text window.

We're almost there, but to make the game run again we need to make changes to the two click functions.

## Changes to ```click_yes(x,y)``` and ```click_no(x,y)```

First we'll change ```click_no(x,y)``` as that's quite simple. If the player clicks the ```no``` turtle, then this function will run, and in it we simply want to close the game. So

- comment out the line of code inside this function by putting a ```#``` at the beginning of the line

- add these lines:

```python
  screen.bye()
  exit()
```

These lines will stop the code running and clear the screen.

Now we need to change ```click_yes(x,y)``` which will run if the player wants to play again. At this point we still have the ```yes``` and ```no``` turtles visible, so we will need to hide these, and also cancel the clicking on these turtles. Then the screen is all clear and ready for the player to make a choice of rock, paper and scissors. All the code for the choice is already written in the function ```make_choice()```, so the final bit of ```click_yes(x,y)``` will be to *call* function  ```make_choice()```.

Start by commenting out the line of code already in this function then add these lines for the ```yes``` turtle:

```python
  yes.hideturtle()
  yes.onclick(None)
```

then add two similar lines for the ```no``` turtle.

Finally add a line to call the function ```make_choice()```:

```python
  make_choice()```
```

Now we're ready to test the code. Run it, play a game, choose to play again, and it should keep repeating until you choose not to play another game.

[Go to Step 5 for trinket](../Step5-Keeping-score-trinket)

[Go back to Step 3](../Step3-Play-the-game-trinket)
