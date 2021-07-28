import random
from art import logo
from replit import clear
print("Welcome to the Number Guessing Game!")


def play():
  print(logo)
  random_number = random.randint(1,100)
  print("I am thinking of a number between 1 and 100")
  user_num = input("Choose a difficulty.Type 'easy' or 'hard':")
  print(user_num)
  if user_num == 'easy':
    attempts = 10
    while attempts >= 1:
      print(f"you have {attempts} attempts remaining to guess the number.")
      attempts -= 1
      guess = int(input("guess the number:"))
      if guess != random_number:
        if guess > random_number:
          print("too high \n Try again!")
          print(f"you have {attempts} attempts remaining to guess the number.")
        elif guess < random_number:
          print("too low \n Try again!")
          print(f"you have {attempts} attempts remaining to guess the number.")
      else:
        print("you got it! you won!")
    print("you lose!")
  if user_num == 'hard':
    attempts = 5
    print("you have 5 attempts remaining to guess the number.")
    while attempts >= 1:
      attempts -= 1
      guess = int(input("guess the number:"))
      if guess != random_number:
        if guess < random_number:
          print("too low\n Try again!")
          print(f"you have {attempts} attempts remaining to guess the number.")
        elif guess > random_number:
          print("too high \n Try again!")
          print(f"you have {attempts} attempts remaining to guess the number.")
      else:
        print("you got it! you won!")
    print("you lose!")

yes_no = input("type 'y' to play and 'n' to quit:")
if yes_no == 'y':
  clear()
  play()
else:
  print("sad to see you go!")
