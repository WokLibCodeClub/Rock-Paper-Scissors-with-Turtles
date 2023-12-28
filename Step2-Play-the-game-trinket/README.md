# Step 2 - Playing the game - trinket

In this step we will write the code for selecting which shape you want to play out of Rock, Paper or Scissors, and for the computer to select one of these shapes at random. We will then show the two shapes together to see who won.

Before we proceed it's a good idea to delete some of the code from the previous step as we will be re-writing those lines:

**_DELETE THESE LINES_**

* the two lines where you set the turtle for your hand to have the shape "you_rock.gif" and the computer turtle to have the shape "computer_scissors.gif";
* the two lines which end ```****.showturtle()```

### Make lists

This project will use Python *lists* in several places. The first two lists we need are for the image files which *you* and the *computer* will use in the game. Make a list for the computer's image files like this:
```
computer_hands = ["computer_rock.gif", "computer_paper.gif", "computer_scissors.gif"]
```

Then add a line to make a similar list, called ```your_hands``` for the shapes for *your* hand. Watch out! The order of the shapes is important, so make sure you have the Rock, Paper and Scissors images in that order.

### Make a global variable

We are going to need a variable to store the choice of Rock, Paper or Scissors that you make for the game. As this variable will be used at different places in the game we need to create it at the top of the code, which will make it a *global* variable - meaning that it can be used everywhere in the project. Add this line of code underneath the code for making the lists:
```
your_choice = -1
```
The global variable is called ```your_choice``` and we have set its value to -1. By setting the value to a number we are telling Python that this is a *numerical* variable. The value will be changed later.


## Define a function for making your choice

Most Python code makes a lot of use of **functions**, so for this project we will put most of the code inside functions. 

To play the game against the computer you have to make a choice of whether to show Rock, Paper or Scissors. We will put the code for this in a function called ```get_choice()```.

Start the definition of the function by adding these two line at the end of your code:
```
def get_choice():
    global your_choice
```
All the code which is part of the function **_MUST BE INDENTED_**.

>### Special Note if you are writing your code with the *Visual Studio Code* editor:
>make sure the line ```mainloop()``` is the *last* line of your code (not indented). Everything should be above that line. 

The first line tells Python that this is the start of a *function*, while the second line tells the function that we will want to use and make changes to the global variable called ```your_choice```.

In the text-only version of the game you make a choice of Rock, Paper or Scissors using the Python ```input()``` statement, and type your answer in the Python shell window. Using the same method in the turtle version would mean having to switch to the Python shell window to make the choice, then switch back to the turtle window to play the game. For the turtle version we can avoid this switching by using the turtle function ```screen.textinput()```.

Add this code to the function and make sure it is indented:
```
    rps = screen.textinput("Your choice!", "rock (r), paper (p) or scissors (s)? ")
```
This instruction opens up a little text box in the top left of the turtle window where you can type in r, p or s (followed by ENTER) for your choice. Whatever you type will be put in a variable called ```rps```.

Next we need to turn your choice into a *number* which we will put in the global variable ```your_choice```. We want the number to be 0 if you chose rock, 1 if you chose paper and 2 if you chose scissors. We can do this with a Python ```if``` block. Here is the start of the block (which is inside the function, so must be indented):
```
    if rps == "r":
        your_choice = 0
    elif rps == "p":
```
You need to complete this block with another **three** lines which will say what will happen if your choice is "p" and if your choice is "s". Watch out for the indentations - some lines are indented *twice*!

## Define a function for playing the game

Now we have coded a function for making a choice we need another function for playing the game. Place this line after all the code for function ```get_choice()```. This line should **not** be indented, otherwise Python will think it is still part of the previous function:
```
def play_game():
```
As before, all the code which is part of this function **_MUST BE INDENTED_**.

### Have the computer make a choice

We don't need to ask the computer what shape to choose - we will use a random number for this. We will put the computer choice in a variable called ```computer_choice``` and select the value using the ```randint()``` function.

Add this as the first line of the function and *indent it* because it is inside the function. This line will take a whole number from 0 to 2 at random and put the value in the variable ```computer_choice```:
```
    computer_choice = randint(0, 2)
```

### Show the choices

Now we need to assign the correct image files to the turtles for your hand and the computer's hand. This is where we will use the image lists we made earlier.

Remember, in a Python list the first item is item 0, so if I had a list of, say, fruits like this:
```
my_fruits = ["banana", "cherry", "orange", "strawberry"]
```
and I wanted to do something with the item "orange" I would refer to this as ```my_fruits[2]```.

### *This is an example list. Don't copy it into your code!!!*

We want to use the lists of images. So if your choice was rock, the variable ```your_choice``` would be set to 0, and we would set the image for your hand to be item 0 of the list of your hand images. If ```your_choice``` is set to 1, then we want item 1 from the image list, and so on. Add this line, *indented* to the end of the function:
```
    ****.shape(your_hands[your_choice])
```
In place of the stars put the name of the turtle you are using for your hand.
Now add another, similar line to set the shape for the computer's hand. You need to get the image name from the other list, and you need to use the variable for the computer's choice, and the name of the turtle you are using for the computer's hand.

Now we've set the turtles to have the right hand shapes we can show the turtles, so **add two lines**, one for each turtle, to show the turtles. Don't forget to indent these lines as they are part of the function.

When you write functions they won't do anything until the functions are *called*. We often do this in the "main" part of the programme, **_which is NOT indented_**. Add this line to call the function get_choice(), at the very end of the code, not indented:
```
get_choice()
```
Now we need to call function ```play_game()```. We could put this at the end, after calling ```get_choice``` but because we always want to run this function after ```get_choice``` a better place is to call it at the end of ```get_choice```. It is very common in Python to have a function calling another function. As the last line of function ```get_choice```, indented, add this:
```
    play_game()
```

Save your code and run it.

Your code should put up a text box to ask you to choose "r", "p" or "s", then show both hands - yours and the computer's. Did you win?

Before we go further there's one little issue we need to tidy up. Good coders always have to assume that the users of their code might make a mistake. So what would happen if someone using your brilliant game accidentally typed in a choice which wasn't "r", "p" or "s"? We'll sort that out on the [next page](README2.md).



