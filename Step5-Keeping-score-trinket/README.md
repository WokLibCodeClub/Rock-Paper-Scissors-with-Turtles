# Step 5 - Keeping the score - Part 1 - trinket

When you play the game many times it would be nice to keep a score, to see who is ahead - you or the computer. The first problem in keeping score is to work out who won the game.

When you look at the two hand shapes for You and Computer you can work out in an instant who has won, but all Python knows is which hand shapes were chosen - it can't tell who was the winner unless you code in the rules of the game. This shows you are more intelligent than a computer!

So there are two parts to writing code to keep score. Obviously we need code to keep track of the two scores, and more code to display the scores on the screen, but before that we have to find a way for Python to work out who has won each game. This page, part 1 of step 4, will cover working out who won, while the next page, part 2 of step 4, will cover the variables for keeping score, and coding a new turtle to display them.

## Working out who won

Remember, from Steps 2 and 3, that for the game we set two variables for you and the computer, called  ```player_choice``` and ```computer_choice```, to store which of rock, paper and scissors the two players had chosen. We used a special code for these two variables: they were set to 0 for *rock*; 1 for *paper* and 2 for *scissors*.

We will put the code for working out the winner inside the function ```play_game()```, just after we have *shown* the two turtles ```player``` and ```computer```. Find this place in your code now. A very good tip would be to put a comment into your code here, like this:

```python
  # work out who won
```

to remind us what the next bit of code will do.

### The long tedious way

Let's say you chose *Rock* (so the variable ```player_choice``` is set to 0) and the computer randomly chose *Scissors* (```computer_choice``` is set to 2). This means You won. We can write this in code using a Python ```if``` block (this code will be inside the function ```play_game()``` so the ```if``` line needs to be indented):

```python
  if player_choice == 0 and computer_choice == 2:
    print('You won!')
```

That deals with who won for one single outcome of the game; unfortunately there are *nine* different possible outcomes of the game (see if you can list them all) and you will have to write a similar ```if``` block with different values and work out who won, or if it was a draw, for *each outcome*.

What a drag!

### The short smart way

There is a much smarter way of coding all possible results using just three lines of code!

If you added the two lines above to your code then you should **delete** these.

Let's look at all the possibilities where ***you beat the computer***:

```python
  your                     computer's                         player_choice minus
 choice   player_choice =      choice      computer_choice =     computer_choice
--------  -------------    ----------    -----------------    ------------------
 Paper          1            Rock                0                 1-0 = 1
Scissors        2            Paper               1                 2-1 = 1
 Rock           0           Scissors             2                 0-2 = -2
```

You can see that when you win, the value of the ```player_choice``` variable is usually bigger than the value of the ```computer_choice``` variable, except for the annoying case where you chose *rock* and the computer chose *scissors*.  One way for Python to tell which of two numbers is bigger is to subtract one from the other: if the answer is positive then the first number is bigger, and if the answer is negative then the second number is bigger. In the last column you can see the answers if you subtract the ```computer_choice``` variable from the ```player_choice``` variable. The answer is always 1, except for the last line, where the answer is -2.

Luckily Python has a clever arithmetic trick which we can use here. When you first learned division you were probably taught to give the answers using a remainder - for example ```7 ÷ 4 = 1, remainder 3```. Now that you know about fractions and decimals you probably never use this elementary method, but in computing the remainders are so useful that Python has a special operator for calculating them. Here is the Python code to show the remainder if I divide 7 by 4. It uses a percentage sign instead of the normal slash sign for division:

```python
7 % 4
```

This is called *modulo division* or *remainder division*. You can experiment with remainder division by typing the line above into a Python console (open [Your Interactive Python Console](https://trinket.io/console)). Try it again, varying the numbers.

It turns out that if we do modulo division by 3 for the numbers 1 and -2, both give the same answer, which is 1:

```python
 1 % 3 = 1
-2 % 3 = 1
```

So if you calculate the subtraction sum ```player_choice - computer_choice``` and do modulo division by 3, if you win the game **it always gives the answer 1**.

```python
  your                      computer's                        player_choice minus     modulo division
 choice   player_choice =       choice     computer_choice =     computer_choice           by 3
--------  ---------------   -----------    -----------------    -----------------     ---------------
 Paper           1              Rock               0                 1-0 = 1            (1-0)%3 = 1
Scissors         2             Paper               1                 2-1 = 1            (2-1)%3 = 1
  Rock           0            Scissors             2                 0-2 = -2           (0-2)%3 = 1
```

We could make another similar table but this time for all the cases where *the computer beats you*. You would find that if you calculate the subtraction sum ```player_choice - computer_choice``` and do modulo division by 3, if the computer wins the game **it always gives the answer 2**.

And if you and the computer choose the same hand shape, then ```player_choice - computer_choice``` gives 0, and modulo division by 3 also gives 0.

So, by doing this bit of maths we can say:

- ```(player_choice - computer_choice)%3 == 0``` means ***it was a draw***
- ```(player_choice - computer_choice)%3 == 1``` means ***You won***
- ```(player_choice - computer_choice)%3 == 2``` means ***Computer won***

using this, here's how to work out who won with only three lines of code:

1. make another list, and put it after the lists of image files, near the beginning of your code:

```python
outcomes = ["It was a draw", "You won", "You lost"]
```

These are the three outcomes which we will print after each game. You can change the text to something else, maybe including smiley faces and sad faces.

2. Inside the function ```play_game```, after the code which shows the two turtles, add this (properly indented):

```python
    result = (player_choice - computer_choice) % 3
    print(outcomes[result])
```

This code first subtracts variable ```computer_choice``` from variable ```player_choice```, then finds the remainder after dividing by three (the brackets are there to ensure Python does the subtraction first). The answer to this sum will be 0 if it was a draw; 1 if you won; 2 if the computer won, and we put this number in a new variable ```result```.

We can now choose which text to print for the result of the game by using the new variable to pick the correct text from our list of outcomes: if ```result``` = 0 it will print item [0] of the list (for a draw); if ```result``` = 1 it will print item [1] of the list (for you winning); if ```result``` = 2 it will print item [2] of the list (for computer winning).

Just three lines of code to cover all the possible combinations.

Save and run your code. The programme will now print out the result in the shell window (with the three >>> signs at the beginning of each line).

Actually, we don't want to print the result to the terminal, we actually want to write the result on the screen. We can use the ```referee``` turtle to do this. **_Instead of_** the print line add these two lines of code:

```python
    sleep(1)
    referee.write(outcomes[result], font = ("arial", 40, "bold"), align = "center")
```

The line ```sleep(1)``` will cause the referee turtle to wait one second before showing the result of the game.

Save your code and test it. You might find that the referee is now writing the text over the top of the two hands. To stop this happening you could alter the position of the referee by adding a ```referee.goto(?,?)``` line before the ```write``` line and choosing suitable coordinates in place of the question marks. If you do this you should also add a line of code before the countdown loop to move the referee back to the centre of the screen for the countdown using, ```referee.goto(0,0)```.

There is one more line of code to add. If you play the game more than once you will see that the referee turtle is still showing the result of the game after you've decided to play again. To stop this happening go to the definition of function ```play_again()``` and in the ```if``` block which begins ```if choice == "y":``` add an additional line ```referee.clear()``` *before* the line ```get_choice()```. This will hide the result of the last game as soon as you choose to play again.

When you are deciding where you want the referee turtle to show the result keep in mind that you need to keep an area of the screen clear to show the score. We will look at coding that on the next page.

[Next page - updating and displaying the score](README2.md)