# Step 6 - Controlling the game using just the mouse - Part 2

We've successfully used turtle-clicking in place of keyboard typing for choosing Rock, Paper or Scissors. Now we need to do something very similar for deciding whether to play again.

For this, we need to rewrite function ```play_again()```.

### Rewrite the function ```play_again()```

Start by _**deleting**_ all the code in function ```play_again()``` except for the first line ```def play_again():```

We will now go through a very similar set of steps to what we did with rewriting function ```get_choice()```.

We will use the referee turtle to give the instruction to the player "Play again? Click y or n:", so put these lines at the beginning of the function definition:

    referee.goto(-350, 300)
    referee.write("Play again? Click y or n:", font = ("arial", 28, 'bold'), align = "left")

Still inside function ```play_again()```, for each of the turtles ```choose_yes``` and ```choose_no``` we need two lines of code to move the turtle to a suitable x,y location and show the turtle. Here is my code for the ```choose_yes``` turtle:
```
    choose_yes.goto(-120, 220)
    choose_yes.showturtle()
```
Now add two similar lines for the turtle ```choose_no``` but you will have to alter the x and y coordinates so you can see the two turtles separately with no overlap. (Try and guess some suitable coordinates for the turtle ```choose_no``` using the coordinate diagram [here](../Step1-Make-Turtles/screen_grid.png). You can always alter them later when you play the game.)

[Go back to previous page: Controlling the game using just the mouse - Part 1](README.md)
