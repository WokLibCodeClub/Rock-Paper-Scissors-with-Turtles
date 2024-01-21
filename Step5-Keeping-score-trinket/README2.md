# Step 5 - Keeping the score - Part 2

## Displaying the who won on the screen

The code up to now is *printing* the result of the game in the text window, but we'd really like to display the result in the graphics area. We can do this using the ```label``` turtle (which we've already used several times to write text onto the screen).

First, though, we need to add a little pause after the two hand shapes are shown, before the computer tells us who has won. So, inside the ```play_game()``` function, after the lines which *show* the ```player``` and ```computer``` turtles, insert this line:

```python
  sleep(1)
```

Now we'll change the ```print()``` line to a turtle ```write()``` line, but before that we'll add a couple of lines to move the ```label``` turtle to a suitable position and set its colour:

```python
  label.goto(0, -80)
  label.color('red)
  label.write(results[result], font = ("arial", 22, 'bold'), align = "center")
```

Save your code and Run it.

Change the position of the ```label``` turtle, or the font for the text if you like.

With the code we've written Python now knows who won each game, so it can use this information to update Your score, and the Computer's score, and display these scores on the screen.

## Keeping track of the score

### New variables

We will obviously keep track of the scores using *variables*. Here, we need *two* new variables - one for Your score and one for the Computer's, and, like the variable ```player_choice```, these need to be *global* variables.

You can decide what to call the variables.

Create them in the **VARIABLES** block of code after the line which creates the ```player_choice``` variable, and **set them both equal to 0**.

These two new 'score' variables are *global* variables, and we want to change the values inside function ```play_game()```. So, find the function ```play_game()``` (which should be in the **FUNCTIONS** block of code), and, as the first line of this function, **insert** a line:

```python
  global ????
```

where, in place of the question marks, ***you have to add the names of your two 'score' variables, separated by a comma***.

### Add code to update scores

In the previous page we set up a little calculation to get the value of the variable ```result```, depending on the result of the game. We used a little code so that

- ```result = 0``` means it was a draw
- ```result = 1``` means You won
- ```result = 2``` means Computer won

We can use the value of ```result``` to make the correct changes to the two 'score' variables, and the way to do this is with two Python ```if``` blocks. Obviously ***if*** ```result``` is 1 we want to increase the player's score by one, and ***if*** ```result``` is 2 we want to increase the computer's score by one, while if ```result``` is 0 it was a draw and we don't need to change either of the scores.

The two Python ```if``` blocks needs to go inside the function ```play_game()``` ***after*** the code which makes the ```label``` turtle write the result of the game.

Can you write Python ```if``` blocks to do this without help? Here are some things to keep in mind

- a Python ```if``` block starts with the word ```if``` and that is followed by code which compares two things - like a variable and a value

- if you want to test if two variables, say ```a``` and ```b``` are the same you need to use a *double* equals sign:

```python
if a == b:
  ```

- don't forget the ```if``` line needs to end with a colon ```:``` and the following lines need to be indented.
- if you want to increase a variable by 1, say it's called ```my_variable``` then the easiest way to code this is

```python
my_variable += 1
```

<details><summary>Hint</summary>

Here is how you could code an ```if``` block to increase the player's score. In this example the variable for the player's score is called ```player_score```:

```python
  if result == 1:
    player_score += 1
```

Now try and write the ```if``` block to increase the computer's score if ```result``` is equal to 2

</details>

<p>

## Displaying the score

Now that we have the updated scores in two variables the only other thing to do is to write the scores on the screen.

### New turtle

We want to keep updating the scores after every game, and we want the scores to be visible all the time. This makes it very complicated to reuse the ```label``` turtle for showing the scores, so the easiest thing is to make a brand new turtle, just for showing the scores. We could call it ```scorer```, but feel free to choose your own name.

Create a turtle called ```scorer``` (or whatever name you like) in the ***VARIABLES*** block of code in the same place as you created the ```yes```, ``no``` and ```label``` turtles.

### New function

We will put the code for displaying the scores in a separate function, as we want to keep calling this function.

Put this function at the end of the ***FUNCTIONS*** block of code. We could call it ```show_scores()```.

2. Add some lines to the end of function ```draw_field``` so the ```background``` turtle will write certain words on the screen. Here is my code for this step, but you might want to change the x and y coordinates and font sizes to suit your layout:
```
    background.goto(-300, -220)
    background.color("black")
    background.write("Score", align = "left", font = ("arial", 32, "normal"))
    background.goto(-220, -270)
    background.write("You", align = "left", font = ("arial", 28, "normal"))
    background.goto(-220, -320)
    background.write("Computer", align = "left", font = ("arial", 28, "normal"))
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Save your code and run it to check the screen layout. Change the coordinates if you need to.

3. Now for writing the scores

We will control writing the scores with a new function called ```update_score()```. Start making this function using the code
```
def update_score():
```
and put it in the section of code where all the other functions are defined.
Here is my code for this function - it uses the ```scorer``` turtle: first, it clears the previous scores, then sends the turtle to an x,y location and writes your score then sends it to a different x, y location and writes the computer score.
```
    scorer.clear()
    scorer.goto(160, -270)
    scorer.write(******, align = "right", font = ("arial", 28, "normal"))
    scorer.goto(160, -320)
    scorer.write(++++++, align = "right", font = ("arial", 28, "normal"))
```
**In place of the asterisks** put the variable name for your score, and **in place of the + signs** put the variable name for the computer's score.

We've written the function, but now we need to **call** it, otherwise nothing will happen. 

First we want to call it when we open the programme, and it will show both the scores as 0. So at the very bottom of the code, just before the line ```get_choice()``` add the line
```
update_score()
```

Secondly we need to call this function at the end of each game. This will be **inside** the function ```play_game()```. Add the same line, (but indented, this time) just before the line ```play_again()```.

Now save the code and run it. Hopefully you now have a functioning graphic Rock, Paper, Scissors game!

You can adjust the x and y locations and the font in function ```update_score()``` to suit your layout, but make sure that the y-coordinate where the ```background``` turtle writes "You" is the same as the y-coordinate where the ```scorer``` turtle writes your score, and the same for the computer's score. That will ensure they line up nicely.


In this version of the game we have used the keyboard to select our hand shape and say whether we want to play again, but many games can be controlled simply by using the mouse, without needing to go to the keyboard at all. We can make a few changes to the code so that you can choose Rock, Paper or Scissors (and whether to play again) simply by clicking on parts of the screen. That is explained in the next step.

That's the end of the project! Play, and enjoy, and may you always beat the computer.

[Back to the introduction](../README.md)

[Go back to Keeping the score - Part 1](README.md)
