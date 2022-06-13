import random
from time import sleep as delay

# function to generate a choice for computer
def generateRandomChoice(choices):
  return random.choice(list(choices.keys()))

# a function to get user input
def getUserInput():
  return input("Press R for Rock, P for Paper, or S for Scissors: ").upper()

# a funcion to generate line breaks (purely aesthetics)
def lineBreak(n):
  return "*"*n

# function to print introduction, etc; runs only once, at the beginning of gameplay
def introduction():
  # display introduction
  print("Welcome to Rock, Paper, Scissors!")
  delay(2)
  print(lineBreak(16))
  print("* HOW TO PLAY: *")
  print(lineBreak(16))
  print("* Choose any option from:\n* R (Rock), \n* P (Paper) or \n* S (Scissors).")
  print(lineBreak(25))
  print("* Rock beats Scissors\n* Scissors beats Paper\n* Paper beats Rock")
  print(lineBreak(25))
  delay(3)
  input("Understood? Press Enter to play:_")
  delay(1)

  gameplay()

def checkForWinner(user_choice, computer_choice, win_list):
  if user_choice in win_list:
    for victor, loser in win_list.items():
      if user_choice == victor and computer_choice == loser:
        return "player"
      
      elif computer_choice == victor and user_choice == loser:
        return "computer"

def gameplay():
  play_game = True
  win_list = {
    "R":"S",
    "P":"R",
    "S":"P"
  }
  
  while play_game == True:
    # prompt user for input
    user_choice = getUserInput()

    if user_choice in win_list:
      # generate random choice for computer
      computer_choice = generateRandomChoice(win_list)
      
      print("Your choice: {} | Computer choice: {}\n".format(user_choice, computer_choice))
    
      # if there is a tie, display message for tie...
      if user_choice == computer_choice:
        print("It\'s a tie! Play again.")

      else:
        #check for winner
        winner = checkForWinner(user_choice, computer_choice, win_list)
        message = "You win!" if winner == "player" else "Sorry! Computer wins! Better luck next time."
        print(message)
        play_game = False
        
    else:
      print("Your input is invalid!\n")
      pass

introduction()


