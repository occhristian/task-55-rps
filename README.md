This RockPaperScissors game is my own solution to I4G assignment, Rock, Paper, Scissors, Task 55.

I used six functions, because I like robust, modular code:

- a function to generate computer's choice, generateRandomChoice()
- a function to get user's input, getUserInput()
- a function for line breaks. I used a lot of asterisks for aesthetics, so I decided to write a separate function for that, lineBreak()
- a function to print the introduction and game help, introduction()
- a function to check the winner in each round, checkForWinner()
- a function to control gameplay, gameplay()

WORKING
Immediately game is initialized, the introduction is printed (only once per init), and then user is giving time to read through it, and game continues after the enter key is pressed.

The getUserInput() function is used to get user's choice, and if their choice is valid, the computer's choice is randomnly generated with the generateRandomChoice() function, else the user is notified that their input is invalid, and gameplay is looped.

As soon as computer's choice is generated, both choices are compared and the winner, returned, using checkForWinner(). The game is then terminated.
