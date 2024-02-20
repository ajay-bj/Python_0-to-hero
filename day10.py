# scope, constants

# scope- apple tree inside our home scope qand outside our boundry(indendation in code)
# local scope vs global scope - it comes under name space
# if we create a variable within a function it works within(local scope),but if,for, while with : then its global scope
# Remember that in Python there is no block scope. Inside a if/else/for/while code block is the same as outside it.
# should not give same name for local & global variable ( or scope )

enemies = 1 #global scope

def increase_enemies():
  enemies = 2 #local scope
  print(f"enemies inside function: {enemies}")#local scope

increase_enemies()
print(f"enemies outside function: {enemies}")#global scope

# modifying withing global scope or global variable
# 
enemies = 1 #global scope

def increase_enemies():
  global enemies # we can modify but dont try to modify gloval scope inside function which has local scope- its to reduce bug or failability
  enemies += 1 #global scope
  print(f"enemies inside function: {enemies}")#

increase_enemies()
print(f"enemies outside function: {enemies}")#global scope
# instead use return to modify- to tap that functionality
enemies = 1 #global scope

def increase_enemies():
  print(f"enemies inside function: {enemies}")
  return enemies + 1

enemies = increase_enemies()# function has returned +1 then is been updated globalvariable here
print(f"enemies outside function: {enemies}")#global scope

# constants and global scope
# we have to be carful using global scope/ it very handy declaring global constants ex: PI = 3.141 etc/ Naming convention is upppercase
PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@yu_angela"# uppercase seperated with underscores

# project
import random 
import randint

logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Pssst, the correct answer is {answer}") 

  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


game()