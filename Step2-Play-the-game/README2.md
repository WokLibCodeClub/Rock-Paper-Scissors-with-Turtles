# Tidying up a loose end...

Inside the function ```get_choice()``` you've written a nice ```if``` block to set the variable ```your_choice``` to 0 if the player typed "r", and 1 if the player typed "p" and 2 if the player typed "s". But what if the player had jittery fingers and accidentally typed a letter or number which wasn't any of these? We need to extend the code for this possibility.

There are lots of ways of doing this. The method here will simply keep showing the input box until the player types one of the three correct options. 

We are using a variable called ```rps``` to store the letter which is typed in by the player. Before the game this variable has no value, but in this method we will give this variable a value before opening the input box.

As the *second* line in function ```get_choice()``` (after the ```global``` line) add this line (don't forget to indent it):
```
    rps = "x"
```

We will now set up a Python ```while``` loop. This is a loop which will test if something is true and keep running as long as the something continues to be true. If the something is no longer true then the loop will finish and the code will go on to the next lines. We will test if the variable ```rps``` has the value "x". To start the ```while``` loop put this code immediately under the line you've just added, and indented to line up with it:
```
    while rps =="x":
```
You may notice that this line ends with a colon, and you may guess what this means about the code which will be inside the while block ... yes, it needs to be indented!

Take all the lines of the if block, and indent them all. This means some lines of the if block will be indented *three times*, once for being inside the function, again for being inside the ```while``` block, and a third time for being inside the ```if``` block.

We need to add a final line to the ```if``` block. This is an ```else:``` line which will say that if the player hasn't typed any of the right letters we should set variable ```rps``` back to "x", so that the loop will run again. The entire ```while``` block should look like this:
```
    rps = "x"
    while rps == "x":
        rps = screen.textinput("Your choice!", "rock (r), paper (p) or scissors (s)? ")
        if rps == "r":
            your_choice = 0
        elif rps == "p":
            your_choice = 1
        elif rps == "s":
            your_choice = 2
        else:
            rps = "x"
```

Save your code and run it. This time try deliberately typing some wrong letters in the box to see what happens. It should keep showing the box until you type one of "r", "p" or "s".

Now that you can see both hands who won? Or was it a draw? Do you remember which hand was yours and which was the computer's? Maybe we should add a bit of extra information to the screen.

[Go to Step 3 - Adding some background and building up the tension](../Step3-Adding-background)

[Go back to previous page](README.md)

