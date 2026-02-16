# Step 5 - Keeping the score - Part 2

## Displaying the who won on the screen

The code up to now is *printing* the result of the game in the text window, but we'd really like to display the result in the graphics area. We can do this using the ```label``` turtle (which we've already used several times to write text onto the screen).

First, though, we need to add a little pause after the two hand shapes are shown, before the computer tells us who has won. So, inside the ```play_game()``` function, after the lines which *show* the two turtles for Your hand and Computer's hand, insert this line:

```python
  sleep(1)
```

Now we'll change the ```print(results[result])``` line to a turtle ```write()``` line, but before that we'll add a couple of lines to move the ```label``` turtle to a suitable position and set its colour:

```python
  label.goto(0, -80)
  label.color('red')
  label.write(results[result], font = ("arial", 22, 'bold'), align = "center")
```

Save your code and Run it.

Change the position of the ```label``` turtle, or the font for the text if you like.

With the code we've written Python now knows who won each game, so it can use this information to update Your score, and the Computer's score, and display these scores on the screen.

## Keeping track of the score

### New variables

We will obviously keep track of the scores using *variables*. Here, we need *two* new variables - one for Your score and one for the Computer's.

You can decide what to call the variables.

Create them in the **SETUP** block of code after the line which creates the ```player_choice``` variable, and **set them both equal to 0**.

These two new 'score' variables are *global* variables, and we want to change the values inside function ```play_game()```. So, find the function ```play_game()``` (which should be in the **FUNCTIONS** block of code), and, as the first line of this function, **insert** a line:

```python
  global ****, ****
```

where, in place of the stars, ***you have to add the names of your two 'score' variables, separated by a comma***.

### Add code to update scores

In the previous page we set up a little calculation to get the value of the variable ```result```, depending on the result of the game. We used a numerical code so that

- ```result = 0``` means it was a draw
- ```result = 1``` means You won
- ```result = 2``` means Computer won

We can use the value of ```result``` to make the correct changes to the two 'score' variables, and the way to do this is with two Python ```if``` blocks. Obviously ***if*** ```result``` is 1 we want to increase the player's score by one, and ***if*** ```result``` is 2 we want to increase the computer's score by one, while if ```result``` is 0 it was a draw and we don't need to change either of the scores.

The two Python ```if``` blocks needs to go inside the function ```play_game()``` ***after*** the code which makes the ```label``` turtle write the result of the game.

Can you write Python ```if``` blocks to do this without help? Here are some things to keep in mind

- a Python ```if``` block starts with the word ```if``` and that is followed by code which compares two things - like a variable and a value

- if you want to test if two variables, say ```a``` and ```b``` are the same you need to use a *double* equals sign:

```python
if a == b:
  ```

- don't forget the ```if``` line needs to end with a colon ```:``` and the following lines need to be indented.
- if you want to increase a variable by 1, say it's called ```my_variable```, then the easiest way to code this is

```python
my_variable += 1
```

<details><summary>Hint</summary>

Here is how you could code an ```if``` block to increase the player's score. In this example the variable for the player's score is called ```player_score```:

```python
  if result == 1:
    player_score += 1
```

Now try and write the ```if``` block to increase the computer's score if ```result``` is equal to 2

</details>

<p>

## Displaying the score

Now that we have the updated scores in two variables the only other thing to do is to write the scores on the screen.

### New turtle

We want to keep updating the scores after every game, and we want the scores to be visible all the time. This makes it very complicated to reuse the ```label``` turtle for showing the scores, so the easiest thing is to make a brand new turtle, just for showing the scores. We could call it ```scorer```, but feel free to choose your own name.

Create a turtle called ```scorer``` (or whatever name you like) in the **SETUP** block of code in the same place as you created the ```yes```, ```no``` and ```label``` turtles.

### New function

We will put the code for displaying the scores in a separate function, as we want to keep calling this function.

Put this function at the end of the **FUNCTIONS** block of code. We could call it ```show_scores()```.

Start with the line to define the function, then put in a line to send the ```scorer``` turtle to a set of x, y coordinates , then a line where this turtle *writes* the text "Score" at these coordinates.

Here is some suggested code with possible x, y coordinates and including parameters for the font style, size and type and the alignment of the text. 

```python
def show_scores():
  scorer.goto(-140,-115)
  scorer.write("Score:", align = "left", font = ("arial", 18, "bold"))
```

The turtle won't write anything until we call the function, so now we'll add code to do that. Go to the section called **MAIN CODE**, where there is just one line so far and put this line in *before* that:

```python
show_scores()
```

This will call the function as soon as you click on Run. If you click on Run you should see the word 'Score' written on the screen.

You can change the text parameters in the ```show_score()```function to your own values to get the word 'Score' to look as you want it. When a turtle is created its colour is set to 'black', so this text appears in black. If you want the text in a different colour you need a line in the function to change the  colour of the ```scorer``` turtle before you *write* the text. (Look for other examples of changing a turtle colour in this project for how to do this.)

Next, we'll add lines to the ```show_score()```function to have the turtle write the words 'You' to the left and 'Computer' to the right, as headers to columns with the scores. Here's some code for writing 'You':

```python
  scorer.goto(-80,-140)
  scorer.write("You", align = "center", font = ("arial", 14, "normal"))
```

Add two more lines with different coordinates to have the turtle write 'Computer' to the right of the word 'You'. You can check the appearance by clicking Run at any time.

Finally we want this turtle to write the variables for your score and the computer's. Here's some possible code for writing your score. ***In place of the stars you need to put the name of your variable for Your score***:

```python
  scorer.goto(-70,-165)
  scorer.write(****, align = "right", font = ("arial", 14, "normal"))
```

Now add two more lines to make the turtle write the Computer's score to the right of Your score. Click Run to check the alignment of the scoreboard, and make any changes to the x, y coordinates or text sizes until you like the result.

We don't just want to *call* this function when we press Run, we want to call it at the end of every game. So, find the function ```play_game()``` and look for the lines where you recalculate your and the computer's scores. Immediately after that line insert

```python
  show_scores()
```

which will run the ```show_scores()``` function after every game.

Click on Run to test your code and keep playing until you get a game which is not a draw.

You might notice that when the score for the winner was updated it didn't delete the number 0 first. This means we need to add one more line to the function ```show_scores()```:

As the *first* line in this function add

```python
  scorer.clear()
```

This will clear all the scorer's annotation including the previous scores. Now test the code again, and you should have a game which keeps the score correctly.

That's the end of the project! Play, and enjoy, and may you always beat the computer.

### Code check

You can have a look at example code for the complete project [here](ex_complete.md).

[Back to the introduction](../README.md)

[Go back to Keeping the score - Part 1](README.md)
