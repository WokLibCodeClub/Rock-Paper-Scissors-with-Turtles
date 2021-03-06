# Step 5 - Keeping the score - Part 1

If you play the game many times it would be nice to keep a score to see if you have won more often than the computer. There are two parts to coding this. Obviously we need to write code to keep track of the two scores, and more code to display the scores on the screen but before that we have to find a way for Python to work out who has won each game.

### Working out who won

If you look at the two hand shapes you can see in an instant who has won, but Python can't tell unless you code in the rules of the game. This shows you are more intelligent than a computer!

Remember, from Step 2, that when you or the computer select *rock* we set the ```your_choice``` or ```computer_choice``` variable to 0; when you or the computer select *paper* we set the ```your_choice``` or ```computer_choice``` variable to 1 and when you or the computer select scissors we set the ```your_choice``` or ```computer_choice``` variable to 2.  

We could use this to work out who won in a very long and clumsy way like this. Lets code the case where you chose *paper* and the computer chose *rock*:
```
if you == 1 and computer == 0:
    print("You won")
```

This ```if``` block tests if two things are true at the same time using the keyword ```and```. You could write a similar ```if``` block for every single possible result of the game (actually there are nine) and work out for each combination if you won, or the computer won, or it was a draw, but this would be rather poor Python coding, as it would create a lot of repetition.

There is a much smarter way of coding all possible results using just three lines of code!

If you added the two lines above to your code then you should **delete** these.

Let's look at all the possibilities where you beat the computer:

```
  your                     computer's                         your_choice minus
 choice   your_choice =      choice      computer_choice =     computer_choice
--------  -------------    ----------    -----------------    ------------------
 Paper          1            Rock                0                 1-0 = 1
Scissors        2            Paper               1                 2-1 = 1
 Rock           0           Scissors             2                 0-2 = -2
```
You can see that when you win the value of the ```your_choice``` variable is bigger than the value of the ```computer_choice``` variable, except for the annoying case where you chose *rock* and the computer chose *scissors*.  One way for Python to tell which of two numbers is bigger is to subtract one from the other: if the answer is positive then the first number is bigger, and if the answer is negative then the second number is bigger. In the last column I have shown the answers if you subtract the ```computer_choice``` variable from the ```your_choice``` variable. The answer is always 1, except for the last line, where the answer is -2.

Luckily Python has a clever arithmetic trick which we can use here. When you first learned division you were probably taught to give the answers using a remainder - for example 7 ÷ 4 = 1, remainder 3. Now that you know about fractions and decimals you probably never use this elementary method, but in computing the remainders are so useful that Python has a special way of quickly calculating them. Here is the Python code to show the remainder if I divide 7 by 4. It uses a percentage sign instead of the normal slash sign for division:
```
7 % 4
```
This is called *modulo division*. If you have a Python shell window (with the >>> prompt at the beginning of each line) you can experiment with remainder calculations by typing in the line above, but varying the two numbers. (If you are using Visual Studio Code, simply type the word python in the terminal window and it will open a Python shell. When you've finished experimenting type exit() to get back to the normal prompt.)

It turns out that if we calculate modulo division by 3 for the numbers 1 and -2 both give the same answer, which is 1. So if you calculate ```your_choice - computer_choice``` for all the cases where you win, and do modulo division by 3 it always gives the answer 1. 

If you make a table like the one above for all the possibilities where the computer beats you you will find that if you calculate 
```your_choice - computer_choice``` and do modulo division by 3 it always gives the answer 2.

And if you and the computer choose the same hand shape, then ```your_choice - computer_choice``` gives 0, and modulo division by 3 also gives 0.

So, using this, here's how to work out who won with only three lines of code:
1. make another list, and put it after the lists of image files, near the beginning of your code:
```
outcomes = ["It was a draw", "You won", "You lost"]
```
These are the three outcomes which we will print after each game. You can change the text to something else, maybe including smiley faces and sad faces.

2. Inside the function ```play_game```, after the code which shows the two turtles, add this (properly indented):

```
    result = (your_choice - computer_choice) % 3
    print(outcomes[result])
```
This code first subtracts variable ```computer_choice``` from variable ```your_choice```, then finds the remainder after dividing by three (the brackets are there to ensure Python does the subtraction first). The answer to this sum will be 0 if it was a draw; 1 if you won; 2 if the computer won, and we put this number in a new variable ```result```.

We can now choose which text to print for the result of the game by using the new variable to pick the correct text from our list of outcomes: if ```result``` = 0 it will print item [0] of the list (for a draw); if ```result``` = 1 it will print item [1] of the list (for you winning); if ```result``` = 2 it will print item [2] of the list (for computer winning).

Just three lines of code to cover all the possible combinations.

Save and run your code. The programme will now print out the result in the shell window (with the three >>> signs at the beginning of each line).

Actually, we don't want to print the result to the terminal, we actually want to write the result on the screen. We can use the ```referee``` turtle to do this. **_Instead of_** the print line add these two lines of code:
```
    sleep(1)
    referee.write(outcomes[result], font = ("arial", 40, "bold"), align = "center")
```

The line ```sleep(1)``` will cause the referee turtle to wait one second before showing the result of the game.

Save your code and test it. You might find that the referee is now writing the text over the top of the two hands. To stop this happening you could alter the position of the referee by adding a ```referee.goto(?,?)``` line before the ```write``` line and choosing suitable coordinates in place of the question marks. If you do this you should also add a line of code before the countdown loop to move the referee back to the centre of the screen for the countdown using, ```referee.goto(0,0)```.

There is one more line of code to add. If you play the game more than once you will see that the referee turtle is still showing the result of the game after you've decided to play again. To stop this happening go to the definition of function ```play_again()``` and in the ```if``` block which begins ```if choice == "y":``` add an additional line ```referee.clear()``` *before* the line ```get_choice()```. This will hide the result of the last game as soon as you choose to play again.

When you are deciding where you want the referee turtle to show the result keep in mind that you need to keep an area of the screen clear to show the score. We will look at coding that on the next page.

[Next page - updating and displaying the score](README2.md)