# Step 4 - Playing again

How can we adjust the code so we can easily play the game again?

We will use another ```while``` loop - the same technique we used in getting the input box to keep appearing until the player typed one of the correct letters. We will introduce a special type of Python variable, called a *Boolean* variable, which can only be set to either ```True``` or ```False```.

Here's how it will work: at the beginning of the game we will set a Boolean variable called ```play``` to ```True```. Then we put the **_whole game_** inside a ```while``` loop which tests if ```play``` is set to ```True```. Then at the end of the game we ask the player whether to play again. If the answer is "yes" we keep the Boolean variable set to ```True```, so the ```while``` loop runs again. If the answer is "no" we change the boolean variable to ```False```, which means the ```while``` loop *won't* run again and the game will end.

[Go to Step 5 - Keeping the score](../Step5-Keeping-score)
