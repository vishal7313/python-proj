from art import logo
import random
from replit import clear

EASY_LEVEL = 10
HARD_LEVEL = 5

def set_turns():
  """Set the number of turns for player to guess"""
  game_type = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if game_type == 'easy':
    return EASY_LEVEL
  else:
    return HARD_LEVEL

def check_answer(guess, computer, turns):
  """Check whether the guess number is lower or higher than random number
  If it is then remove one turn"""
  if (guess > computer):
    print("Thinking lower number")
    return turns - 1
  elif (guess < computer):
    print("Thinking higher number")
    return turns - 1
  else:
    print("You got the correct number")

  
def game():
  clear()
  print(logo)
  print("Welcome to the number gusseing game\n")
  print("I am thinking of a number between 1 to 100\n")
  computer_num = random.randint(1, 100)

  turns =  set_turns()
  guess_num = 0;
  while guess_num != computer_num:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess_num = int(input("Make a guess: "))

    turns = check_answer(guess_num, computer_num, turns)

    if (turns == 0):
      print(f"You ran out of turns")
      return
    elif guess_num != computer_num:
      print("Guess Again")

game()