# Step 3 - Playing the game - trinket

In this step we'll add the code to get a basic game between *you* and *the computer* up and running. Later we'll write code so that the computer can work out who won, and keep the score in case you want to play more than once.

To do this we'll have to rearrange some of the code we've already written and organise it into Python ***functions***.

## Functions for Rock Paper Scissors

We'll start by making two functions, one to handle the player making a choice of which hand to play, and one to handle showing your choice next to the computer's choice. We'll write the second one first!

### Function for playing the game

This function will be called ```play_game()``` and we put the code in the section with the heading **FUNCTIONS**. You should already have three functions in this section - for controlling what happens when the player clicks either the Rock, Paper or Scissors hand shape, so after these functions put

```python
def play_game():
  global computer_choice
```

```computer_choice``` is a variable we haven't yet made, but when we do make it we need it to be a *global variable*, so we need the second line here.

At the moment we still have the three choose turtles visible, so the first thing to do in the play_game function is to hide these:

```python
  choose_rock.hideturtle()
```

Now add two more lines to hide the other two choose turtles.

But even though these turtles are hidden it turns out you can still click on them! So, next, we need to cancel turtle-clicking for these three turtles:

```python
  choose_rock.onclick(None)
```

Now add two more lines for the other two choose turtles.

#### Have the computer make a choice

We don't need to ask the computer what shape to choose - we will use a random number for this. We will put the computer choice in a variable called ```computer_choice``` and select the value using the ```randint()``` function.

Add this as the next line of the function:

```python
  computer_choice = randint(0, 2)
```

This line chooses a whole number from 0 to 2 at random and puts the value in the variable ```computer_choice```:

#### Setting the shape for the ```player``` and ```computer``` turtles

At this point we know what the ```player_choice``` is, because the player has chosen it by clicking on a choose turtle, and we have a randomly generated a value for the ```computer_choice```, so now we can show the player and computer turtles and see who won. But first, we need to set the correct *shape* for these two turtles.

This is done using the two *lists* we made earlier, called ```player_hands``` and ```computer_hands```.

We have used a code for the variables ```player_choice``` and ```computer_choice``` where 0 = Rock, 1 = Paper and 2 = Scissors. These numbers correspond to the *index* numbers in the lists for the image files for rock, paper and scissors, so if we had player choice set to 1, then the correct image file to use would be ```player_hands[1]```. This means we can use the ```player_choice``` variable as the *index* for these lists to set the correct shape. Here's how we do it for the player's hand. This will be the next line in the function:

```python
  player.shape(player_hands[player_choice])
```

Now add another line to set the computer hand shape.

Finally, we *show* the two turtles:

```python
  player.showturtle()
```

Add the line to show the computer turtle.

That's the end of the ```play_game()``` function, but none of the code will run because we haven't *called* the function anywhere.

### Adjusting the ```def_click``` functions

Also in the section called **FUNCTIONS** are three onclick functions, and the last line of each of these is ```print(player_choice)```. We put this line in as a check that clicking on the turtle produced the correct value for ```player_choice```. However, we don't need it for the game. Instead we can substitute a line here which *calls* the ```play_game()``` function:

```python
  play_game()
```

Make this substitution in *each* of the three onclick functions.

Now we have a game which should work: when the player clicks a turtle to choose a hand it will run the ```play_game()``` function and display the player and turtle hands.

Click on Run to try it. Run the code several times to check it's working for all choices. How often did you win?

### Function for making the player's choice

With the code as it is so far, we don't actually need to make a function for the player to choose a hand, but if we extend the code to play the game more than once it will be very useful to have this code in a separate function.

We'll call this function ```make_choice()```. Put the code right after function ```play_game()```.

```python
def make_choice():
  ```

We don't have to write any new code for this function - we merely have to *move* some lines from other parts of the project.

First, take the three lines in the **MAIN CODE** section and move them to inside the function ```make_choice()```. Don't forget, you will have to *indent* these lines to make them part of the function.

These are the lines which set up the ```onclick``` functions for the three choose turtles.

Next, find the three lines which *show* the choose turtles. These will probably be just after the lines which set the positions of these turtles. Move the ```showturtle()``` lines to the end of function ```make_choice()``` and don't forget to indent them.

That's all we need for the function, but the code won't work now, because we haven't *called* this function. So add this line in the (now empty) section labelled **MAIN CODE**:

```python
make_choice()
```

so that when we click Run, it calls the ```make_choice()``` function.

Run the code to check it works as it did before.

## Add some annotation

At the moment the game ends with just two turtles on the screen, so it would be nice to put some labels to show which hand is yours and which is the computer's. For this we will make another turtle. We can use the same turtle for several other bits of labelling in the game, so it will be a very useful animal.

I'll call the turtle ```label``` but you can choose a different name if you want. Add this line after the lines which create the choose turtles. Make sure you put it *before* the ```for``` loop, so this new turtle will get all the same settings as the other turtles.

```python
label = Turtle()
```

### Labelling the player's and computer's hands

We'll put this turtle to work in the ```play_game()``` function. Just *before* we show the player and computer turtles here is one way to add the labels:

```python
  label.clear()
  label.color('green')
  label.goto(-80, 50)
  label.write('You', font = ("arial", 18, 'normal'), align = "center")
  label.color('blue')
  label.goto(80, 50)
  label.write('Computer', font = ("arial", 18, 'normal'), align = "center")
```

Run the code to see what it does. You should see the words "You" and "Computer" on the screen near the two hands. Are these words in the right place? Do you like the colours? Is the font the right size? Feel free to change this bit of code to suit your game by adjusting the coordinates in the ```goto()``` lines, or the colours or anything in the ```write()``` lines.

### Adding instructions for choosing a hand

We'll use the same turtle in the ```make_choice()``` function to add some instructions. At the end of this function add:

```python
  label.clear()
  label.color('black')
  label.goto(-210, 160)
  label.write('Click shape to choose rock, paper or scissors', font = ("arial", 14, 'bold'), align = "left")
```

### Building up the tension

Let's use the ```label``` turtle for another task: we could put in a 3, 2, 1 countdown before we show the player and computer hands, to build up the tension.

Put this code in the ```play_game()``` function *after* the code to set the shapes of the player and computer turtles:

```python
   for n in range(3):
    label.clear()
    label.color('red')
    label.goto(0,0)
    label.write(str(n), font = ("arial", 48, 'bold'), align = "center")
    sleep(1)
```

Run the code. This little ```for``` loop will run three times (```range(3)```) and will write big red numbers in the middle of the screen. Each time it goes through the loop will wait one second (```sleep(1)```) before continuing with the loop. After the loop has run three times the two player and computer hands will be shown.

But our code is writing 0, 1, 2 on the screen, where we wanted it to write 3, 2, 1. Why is that?

You might remember that the command ```range(3)``` generates a list ```[0, 1, 2]```, so this loop takes a variable called ```n``` and sets it, in turn, to 0, 1 and 2. Our ```label``` turtle is set to write the value of ```n``` (which has to be converted to a string first) each time. So whatever list the ```range()``` function makes, those are the numbers that will be written. If you change the ```range()``` function you can get different numbers.

Can you work out how to change the ```range()``` function so it will generate ```[3, 2, 1]``` instead of ```[0, 1, 2]```?

But 

