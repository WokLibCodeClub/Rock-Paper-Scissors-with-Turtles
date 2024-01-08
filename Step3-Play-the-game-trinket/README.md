Tasks:

change print(player_choice) to play_game() x 3

write play_game()
- set computer_choice using randint
- hide the three choose turtles
- set the onclick to None
- set costumes for player and computer
- show the player and computer turtles

add annotation turtle and 

# Playing the game - trinket

In this step we'll add the code to get a basic game up and running between *you* and *the computer*. Later we'll write code so that the computer can work out who won, and keep the score in case you want to keep playing more than once.

To do this we'll have to rearrange some of the code we've already written and organise it into Python ***functions***.

## Functions for Rock Paper Scissors

We'll start by making two functions, one to handle the player making a choice of which hand to play, and one to handle showing your choice next to the computer's choice. We'll write the second one first!

### Function for playing the game

This function will be called ```play_game()``` and we put the code in the section with the heading **FUNCTIONS**. You should already have three functions in this section - for controlling what happens when the player clicks either the Rock, Paper or Scissors hand shape, so after these functions put

```python
def play_game():
  global computer_choice
```

```computer_choice``` is a variable we havne't yet made, but when we do make it we need it to be a *global variable*, so we need the second line here.

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

### Adjusting the ```def_click``` functions



### Function for making the player's choice

Well call this function ```make_choice()``` and put the code right after function ```play_game()```.


## Add some annotation

At the moment we just have two turtles on the screen, so it would be good to put some labels to show which is which.