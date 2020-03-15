# Step 3 - Adding some background and building up the tension...

What if you forget which hand is yours and which is the computer's? We need to add a bit of annotation to the window to keep things straight.

Also, in our game so far, the two turtle hands appear as soon as you've made your choice. It would be a bit more exciting if we had a short delay, to build up the tension. Maybe we could have a countdown - 3, 2, 1 - appear on the screen before showing the turtle hands.

We will make two new turtles, one to draw some background information, and another to show us a countdown. We will also make another function.

### Window extra information

We start with making a turtle to draw the background. I've called mine ```background```.

In the part of code where you made turtles for your hand and the computer's hand add lines to make this new turtle:
```
background = Turtle()
```
then add lines to **hide** this turtle, and to set it to **penup**.

Now, before the line ```def play_game():```, define a new function:
```
def draw_field():
```
Inside this function we want to tell the turtle ```background``` to write the words "You" and "Computer" just above where the two hands will appear. You can use a different colour for each word, and you need to find out by experiment where to position the turtle before it writes the words. Here is the code, and you need to fill in coordinates in place of the question marks, and colours in place of the stars. You can change the font as well if you like.

```
    background.goto(?, ?)
    background.color("***")
    background.write("You", font = ("arial", 24, "italic"), align = "center")
    background.goto(?, ?)
    background.color("***")
    background.write("Computer", font = ("arial", 24, "italic"), align = "center")
```
As for all functions this function won't do anything until you **call** it. To call this function add a new line at the end of the code, **_just before_** the line which calls function ```play_game()```. This line will call the ```draw_field()``` function and will look like this:
```
draw_field()
```

Save your code and run it. If the words "You" and "Computer" are not in the right place you need to adjust the coordinates. At least now it's clear which hand is you and which is the computer. Did you win this time? 

### Displaying a countdown

Now for another new turtle to give us a countdown. I've called mine ```referee```. Go to the part of code where you define all the other turtles and add three new lines - one to create the referee turtle, one to **hide** it, and one to set it to **penup**.

The code for the countdown will be **INSIDE** the function ```play_game()```. Find the place in this function after you have chosen "r", "p" or "s", and after the computer's choice has been made from a random number, but **before** you set up the turtle shapes. Insert this code to make a Python *repeat* loop: 
```
    for i in [3, 2, 1]:
        referee.color("red")
        referee.write(i, font = ("arial", 100, "bold"), align = "center")
        sleep(1)
```
This Python repeat loop uses a Python **_list_**, which is a list of items in square brackets, separated by commas. Our list here is very simple, and contains the numbers 3, 2 and 1. The first time Python runs this repeat loop it sets a variable called ```i``` to be equal to the first item in the list. The referee turtle writes the number contained in the variable ```i```, and then waits for one second. The *next* time through the loop the variable ```i``` is set to be equal to the *second* item in the list and does the same operations. The *third* time through the loop variable ```i``` is set to be equal to the *third* item in the list. Python will then go back to the start of the loop but it will find that there are no more values in the list, so the loop will stop.

Save the code and run it. 

There seems to be a problem - the countdown numbers are printing on top of one another. You need to add a line into the loop which will clear the previous number. The code is ```referee.clear()``` - but where exactly in the loop will you put it?

Save the code and test it, and see how it adds a bit of excitement waiting to see what hand the computer will show. Did you win?

Even with the countdown the game is over very quickly. If you wanted another go, especially if you lost, you'd have to close the turtle window and start the code again, which is not very handy. Much better to build something into the code to allow the game to keep repeating if we want to play again.

[Go to Step 4 - Playing again](../Step4-Play-again)
