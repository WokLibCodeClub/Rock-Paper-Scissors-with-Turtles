# Step 5 - Keeping the score - Part 2

We've now written code so Python knows who won each game. The next steps are to use this information to keep track of Your score, and the Computer's score, and display these scores on the screen.

### Keeping track of the score

If you've ever written a Scratch programme which has a score you will know that the way to keep track of a score is to put the score in a *variable*. Here, we need *two* variables - one for your score and one for the computer's.

Near the top of the code, before the function definitions, **add two lines** which will set these two variables to zero.

Because these variables have been declared at the top of the code (not indented) they are called *global* variables. But we want to use these variables inside function ```play_game()```. In order that this function knows which variables we are referring to we need to insert a line as the first line of this function:
```
    global 
```
where after the word global **_you have to add the names of your two score variables, separated by a comma_**.

We will use the result of the game to increase the score variables. Add some code **inside** function ```play_game()``` after the line where the referee turtle writes the result of the game but **before** the line ```play_again()```. 

The code you add will be an ```if``` block. The ```if``` block must do two things - if you won then it should add 1 to your score, if the computer won then it should add 1 to the computer's score. If it was a draw then there's no need to change either variable.

* Your ```if``` block code will have to look at the variable called ```result``` and make decisions depending on what this variable is set to.

* There are two ways to add 1 to a variable in Python. The basic way is
```
my_variable = my_variable + 1
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;where this will take the value of a variable called ```my_variable``` at the moment, add one to it and put the answer back into the same variable. 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;But this is something you do so often in Python that there is a Python shortcut to do exactly the same thing, but with less typing:
```
my_variable += 1
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use whichever version you like in your ```if``` block.

### Displaying the score

Now that we have the updated scores in two variables the only other thing to do is to write the scores on the screen.

We will use the ```background``` turtle to draw the headings for the scores but we will need a separate new turtle to display the scores - this because we want to draw the background *once*, at the beginning, but we want to keep updating the score after each game. The best way to do these two tasks is to have a different turtle for each.

1. In the code where you make all the turtles make a new turtle, maybe called ```scorer```, and, as usual, hide it, and set it to penup.

2. Add some lines to the end of function ```draw_field``` so the ```background``` turtle will write certain words on the screen. Here is my code for this step, but you might want to change the x and y coordinates and font sizes to suit your layout:
```
    background.goto(-300, -220)
    background.color("black")
    background.write("Score", align = "left", font = ('arial', 32, "normal"))
    background.goto(-220, -270)
    background.write("You", align = "left", font = ('arial', 28, "normal"))
    background.goto(-220, -320)
    background.write("Computer", align = "left", font = ('arial', 28, "normal"))
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Save your code and run it to check the screen layout.

3. Now for writing the scores


In this version of the game we use the keyboard to select our hand shape and say whether we want to play again, but many games can be controlled simply by using the mouse, without needing to go to the keyboard at all. We can make a few changes to the code so far so that you can choose Rock, Paper or Scissors (and whether to play again), simply by clicking on parts of the screen. That is in the next step.

[Go to Step 6 - Controlling the game using just the mouse](../Step6-Mouse-control)

[Go back to Keeping the score - Part 1](README.md)
