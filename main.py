import random
from art import logo
from replit import clear

random_number = random.randint(1,100)

easy_turns = 10
hard_turns = 5

def check(guess,random_number, attempts):
  if guess > random_number:
    print("too high! \nTry again!") 
    return attempts - 1 
  elif guess < random_number:
    print("too low! \nTry again!")
    return attempts - 1 
  else:
    print(f"you got it! The answer was {random_number}")


def level_difficulty():
  user_level = input("Choose a difficulty.Type 'easy' or 'hard':")
  if user_level == 'easy':
    return easy_turns
  elif user_level == 'hard':
    return hard_turns

def game():
  print("Welcome to the Number Guessing Game!")
  print("I am thinking of a number between 1 and 100")
  print(f"psss. the correct number is {random_number}")
  attempts = level_difficulty()
  guess = 0
  while guess != random_number:
    print(f"you have {attempts} attempts remaining to guess the number")
    guess = int(input("guess the number:"))
    attempts = check(guess,random_number,attempts)
    if attempts == 0:
      print("You lost!")
      return
 
game()
yes_no = input("type 'y' to play and 'n' to quit:")
if yes_no == 'y':
  clear()
  game()
else:
  print("sad to see you go!")
