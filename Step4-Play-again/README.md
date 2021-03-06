# Step 4 - Playing again

How can we adjust the code so we can easily play the game again?

We'll make another function to take care of asking if the player wants to play again.

After all the code for defining function ```draw_field()``` define our new function ```play_again()```. The first line is
```
def play_again():
```
Inside this function (DON'T FORGET TO INDENT THE CODE) we can use very similar code to the lines which we used to get the player's input of "r", "p", or "s". 

* Start with setting a variable called ```choice``` to "x". 
* Then put in a ```while``` loop which tests if ```choice``` is equal to "x".
* Inside the ```while``` loop (indented) put a line which sets choice equal to the result of a ```screen.textinput()``` line where you ask the player to choose "y" or "n" for whether to play again. (Check the other ```textinput``` line for "r", "p" or "s" to remind yourself how to do this.)
* Next make an ```if``` block with different options depending on whether the player typed "y" or "n". It should look like this:
```
        if choice == "y":
            you.hideturtle()
            computer.hideturtle()
            get_choice()
        elif choice == "n":
            screen.bye()
            exit()
        else:
            choice = "x"
```
If the player typed "y" the code will clear the hand images, then call the function ```get_choice()``` which will start the game again.
If the player typed "n" the code will close the turtle window, then exit the program.
If the player didn't type "y" or "n" the variable ```choice``` will be set back to "x", so the ```while``` loop will run again and ask the question again.

>### Special Note if you are writing your code with the *Visual Studio Code* editor:
>
>Leave out the line ```screen.bye()``` as this will cause an error, and the window will close properly without it.


That's the job of defining the new function done. But nothing will happen until we call this function. We call this function as the *very last line* of function ```play_game()``` with the line
```
    play_again()
```
Make sure this line is indented to be level with the other code in function ```play_game()```.

Save your code and test it. Try typing "y" and "n" when you get asked the question about playing again, and also test typing a letter that's not "y" or "n" to check that your code keeps displaying the question until you do type y" or "n".


Now that it's so easy to restart the game you might find you want to keep playing it. But are you ahead of the computer or is the computer winning? We need to find a way of keeping the score.

[Go to Step 5 - Keeping the score](../Step5-Keeping-score)
