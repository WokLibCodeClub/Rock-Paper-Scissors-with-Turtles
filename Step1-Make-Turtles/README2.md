# Making smarter code

You just made two turtles, and for each turtle you typed in the same code - to **hide** the turtle, set it to **penup** and set its speed to **speed(0)**.

Later in the game you will be making up to eight more turtles, and for each one you will want the same three instructions - that's a lot of typing, especially as almost all the typing can be avoided by using a Python *repeat loop*.

## Using a Python ```for``` loop

This is the Python equivalent of a Scratch *Repeat* loop. The loop begins with code like this:
```
for i in *******:
```
i is a variable, used in the loop, and instead of the asterisks we give the loop a **list** of items. The first time through the loop Python sets variable ```i``` to the first item in the list, the second time through the loop it sets variable ```i``` to the second item in the list, and so on, until all the items in the list have been used once. Then the loop stops.

**All the code which is part of the loop must be indented!**

Here the list is going to contain all the turtles in the project (at the moment there are only two, but there will be many more later). And the operations, inside the loop, will be to set every turtle to **hide**, **penup** and **speed(0)**.

Luckily Python gives a simple method to make a list of all the turtles in a project. Here is the code for the complete loop. This code needs to go **after** the lines which create the turtles:
```
for i in screen.turtles():
    i.hideturtle()
    i.penup()
    i.speed(0)
```
You should now **delete** the lines you added before to set properties for each of the two turtles, because these instructions will now be handled by the loop.
```
****.hideturtle()
****.penup()
****.speed(0)
```

Now we can get going with coding the game.

[Go to Step 2 - Playing the game](../Step2-Play-the-game)

[Go back to previous page](README.md)
