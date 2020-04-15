# Step 6 - Controlling the game using just the mouse - Part 2

We've successfully used turtle-clicking in place of keyboard typing for choosing Rock, Paper or Scissors. Now we need to do something very similar for deciding whether to play again.

For this, we need to rewrite function ```play_again()```.

### Rewrite the function ```play_again()```

Start by _**deleting**_ all the code in function ```play_again()``` except for the first line ```def play_again():```

We will now go through a very similar set of steps to what we did with rewriting function ```get_choice()```.

We will use the referee turtle to give the instruction to the player "Play again? Click y or n:", so put these lines at the beginning of the function definition:
```
    referee.goto(-350, 300)
    referee.write("Play again? Click y or n:", font = ("arial", 28, 'bold'), align = "left")
```
Still inside function ```play_again()```, for each of the turtles ```choose_yes``` and ```choose_no``` we need two lines of code to move the turtle to a suitable x,y location and show the turtle. Here is my code for the ```choose_yes``` turtle:
```
    choose_yes.goto(-120, 220)
    choose_yes.showturtle()
```
Now add two similar lines for the turtle ```choose_no``` but you will have to alter the x and y coordinates so you can see the two turtles separately with no overlap. (Try and guess some suitable coordinates for the turtle ```choose_no``` using the coordinate diagram [here](../Step1-Make-Turtles/screen_grid.png). You can always alter them later when you play the game.)

For each of these two turtles we need to write code to say what will happen when we click on the turtle. As on the previous page, we will do this by adding an ```onclick``` command for each turtle. Then, we need to code the two new functions. Here is how I made the code for clicking on the ```choose_yes``` turtle. You need to add similar code for the ```choose_no``` turtle.
1. inside the function ```play_again()``` add this line (indented)
```
    choose_yes.onclick(yes_click)
```
2. at the end of the section containing function definitions add a new function:
```
def yes_click(x,y):
    you.hideturtle()
    computer.hideturtle()
    referee.clear()
    get_choice()
```
This is the function which will run when you click on Yes to play again, so it needs to do the same jobs which we did in the keyboard version inside function ```play_again()```. This code hides the hand shapes for *you* and *computer*, clears the text written by the referee turtle to say who won, then calls function ```get_choice``` to start a new game.

When you write the code for turtle ```choose_no``` you need to see what happened in the keyboard version when the player selected "No" to end the game, and put these steps inside your ```no_click()``` function.

The last job is to add code to the beginning of function ```get_choice``` which will hide the *Yes* and *No* turtles, and disable clicking on these turtles. Add this code (indented) to the top of function ```get_choice()``` for the turtle ```choose_yes```:
```
    choose_yes.hideturtle()
    choose_yes.onclick(None)
```

then underneath these two lines add two more to do the same jobs for turtle ```choose_no```.



[Go back to previous page: Controlling the game using just the mouse - Part 1](README.md)
