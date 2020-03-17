# Step 5 - Keeping the score - Part 2

We've now written code so Python knows who won each game. The next steps are to use this information to keep track of Your score, and the Computer's score, and display these scores on the screen.

### Keeping track of the score

If you've ever written a Scratch programme which has a score you will know that the way to keep track of a score is to put the score in a *variable*. Here, we need *two* variables - one for your score and one for the computer's.

Near the top of the code, before the function definitions, **add two lines** which will set these two variables to zero.

We will use the result of the game to increase the score variables. Add some code **inside** function ```play_game()``` after the line where the referee turtle writes the result of the game but **before** the line ```play_again()```. 

The code you add will be an ```if``` block. The ```if``` block must do two things - if you won then it should add 1 to your score, if the computer won then it should add 1 to the computer's score. If it was a draw then there's no need to change either variable.

* Your ```if``` block code will have to look at the variable called ```result``` and make decisions depending on what this variable is set to.

* There are two ways to add 1 to a variable in Python. The basic way is
```
my_variable = my_variable + 1
```
where this will take the value of a variable called ```my_variable``` at the moment, add one to it and put the answer back into the same variable. But this is something you do so often in Python that there is a Python shortcut to do exactly the same thing, but with less typing:
```
my_variable += 1
```

Use whichever version you like in your ```if``` block.

### Displaying the score


In this version of the game we use the keyboard to select our hand shape and say whether we want to play again, but many games can be controlled simply by using the mouse, without needing to go to the keyboard at all. We can make a few changes to the code so far so that you can choose Rock, Paper or Scissors (and whether to play again), simply by clicking on parts of the screen. That is in the next step.

[Go to Step 6 - Controlling the game using just the mouse](../Step6-Mouse-control)

[Go back to Keeping the score - Part 1](README.md)
