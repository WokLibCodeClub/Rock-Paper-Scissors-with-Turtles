# Step 2 - Playing the game

In this step we will write the code for selecting which shape you want to play out of Rock, Paper or Scissors, and for the computer to select one of these shapes at random. We will then show the two shapes together and try and work out who won.

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

## Define a function for playing the game

Most Python code makes a lot of use of **functions**, so for this project we will put most of the code inside functions. 

Here is the code for defining a function for playing the game. Place this line at the end of your code:
```
def play_game():
```
>### Special Note if you are writing your code with the *Visual Studio Code* editor:
>you need the line ```mainloop()``` as the *last* line of your code. Everything on this page should be above that line.

In this example the function is called ```play_game()``` but you can use a different name if you like.

All the code which is part of the function **_MUST BE INDENTED_**.

### Make your choice

In the text-only version of the game you make a choice of Rock, Paper or Scissors using the Python ```input()``` statement. For the turtle version this would mean having to switch to the Python shell window to make the choice, then switch back to the turtle window to play the game. For the turtle version we can use the turtle function ```screen.textinput()```.

Put this code under the line which defines the function and make sure it is indented:
```
    rps = screen.textinput("Your choice!", "rock (r), paper (p) or scissors (s)? ")
```
This will open up a little text box in the top left of the turtle window where you can type in r, p or s (followed by ENTER) for your choice. Whatever you type will be put in a variable called ```rps```.

Next we need to turn your choice into a number which we will put in a numerical variable called ```your_choice```. We want the number to be 0 if you chose rock, 1 if you chose paper and 2 if you chose scissors. We can do this with a Python ```if``` block. Here is the start of the block (which is inside the function, so must be indented):
```
    if rps == "r":
        your_choice = 0
    elif rps == "p":
```
You need to complete this block with another three lines which will say what will happen if your choice is "p" and if your choice is "s". Watch out for the indentations - some lines are indented *twice*!

### Have the computer make a choice

We don't need to ask the computer what shape to choose - we will use a random number for this. We will put the computer choice in a variable called ```computer_choice``` and select the value using the ```randint()``` function.

Add this line to the end of the code and *indent it* because it is inside the function. This line will take a whole number from 0 to 2 at random and put the value in the variable ```computer_choice```:
```
    computer_choice = randint(0, 2)
```

### Show the choices

Now we need to assign the correct image files to the turtles for your hand and the computer's hand. This is where we will use the image lists we made earlier.

Remember, in a Python list the first item is item 0, so if I had a list of, say, fruits like this:
```
my_fruits = ["banana", "cherry", "orange", "strawberry"] # this is an example list. Don't copy it into your code!!!
```
and I wanted to do something with the item "orange" I would refer to this as ```my_fruits[2]```.

We want to use the lists of images. So if your choice was rock, the variable ```your_choice``` would be set to 0, and we would set the image for your hand to be item 0 of the list of your hand images. If ```your_choice``` is set to 1, then we want item 1 from the image list, and so on. Add this line, *indented* to the end of the function:
```
    ****.shape(your_hands[your_choice])
```
In place of the stars put the name of the turtle you are using for your hand.
Now add another, similar line to set the shape for the computer's hand. You need to get the image name from the other list, and you need to use the variable for the computer's choice, and the name of the turtle you are using for the computer's hand.

Now we've set the turtles to have the right hand shapes we can show the turtles, so **add two lines**, one for each turtle, to show the turtles. Don't forget to indent these lines as they are part of the function.

When you write a function it won't do anything until the function is *called*. We do this in the "main" part of the programme, **_which is NOT indented_**. Add this line to call the function play_game, at the very end of the code, not indented:
```
play_game()
```

Save your code and run it.

### Who won?



[Go to Step 3 - Adding some background information](../Step3-Adding-background)
