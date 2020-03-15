# Step 5 - Keeping the score - Part 1

If you play the game many times it would be nice to keep a score to see if you have won more often than the computer. There are two parts to this. Obviously we need to write code to keep track of the two scores, and more code to display the scores on the screen but before that we have to find a way for Python to work out who has won each game.

### Working out who won

If you look at the two hand shapes you can see in an instant who has won, but Python can't tell unless you code in the rules of the game. This shows you are more intelligent than a computer!

Remember, from Step 2, that when you or the computer select *rock* we set the ```you``` or ```computer``` variable to 0; when you or the computer select *paper* we set the ```you``` or ```computer``` variable to 1 and when you or the computer select scissors we set the ```you``` or ```computer``` variable to 2.  

We can use this to work out who won in a very long and clumsy way like this. Lets code the case where you chose *paper* and the computer chose *rock*:
```
if you == 1 and computer == 0:
    print("You won")
```

This ```if``` block tests if two things are true at the same time using the keyword ```and```. You could write a similar ```if``` block for every single possible result of the game (actually there are nine) and work out for each combination if you won, or the computer won, or it was a draw, but this would be rather poor Python coding, as it would create a lot of repetition.

There is a much smarter way of coding all possible results using just a couple of lines of code!

Let's look at all the possibilities where you beat the computer:

```
 your      your    computer's    computer's        your number minus
choice    number     choice        number          computer's number
------    ------   ----------    ----------        -----------------
 Paper       1        Rock            0                 1-0 = 1
Scissors     2        Paper           1                 2-1 = 1
 Rock        0       Scissors         2                 0-2 = -2
```
You can see that when you win your number is bigger than the computer's number, except for the annoying case where you chose *rock* and the computer chose *scissors*.  One way for Python to tell which of two numbers is bigger is to subtract one from the other: if the answer is positive then the first number is bigger, and if the answer is negative then the second number is bigger. In the last column I have shown the answers if you subtract the computer's number from your number. The answer is always 1, except for the last line, where the answer is -2.

Luckily Python has a clever arithmetic trick which we can use here. When you first learned division you were probably taught to give the answers using a remainder - for example 7 ÷ 4 = 1, remainder 3. Now that you know about fractions and decimals you probably never use this elementary method, but in computing the remainders are so useful that Python has a special way of quickly calculating them. This Python code will tell me the remainder if I divide 7 by 4, using a percentage sign instead of the normal slash sign for division:
```
7 % 4
```
This is called modulo division.


[next page - updating and displaying the score](README2.md)