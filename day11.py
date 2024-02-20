###########DEBUGGING#####################
# ASK STACK OVERFLOW AND ORACAL 

# 1 # Describe Problem
def my_function():
  for i in range(1, 20): # 20 INSTEAR OF 21
    if i == 20:
      print("You got it")
# my_function()

# 2 # Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6) # 6 IS THE ISSUE IT HAS TO BE 5
print(dice_imgs[dice_num])

# 3 # Play Computer
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year > 1994:# >= REPLACE
  print("You are a Gen Z.")

# 4 # Fix the Errors
age = input("How old are you?")# ITS STRING WE HAVE TO TYPE CAST (INT(INPUT ("How old are you?")))
if age > 18:
print("You can drive at age {age}.")# INDENDATION bug , fSTRING NIT ADDED

# 5 #Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: ")) # ==( SO BECAME 0) IS THE ISSUE IT HAS TO BE =
total_words = pages * word_per_page
print(total_words)

# 6 #Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
  b_list.append(new_item) # INDENDAATION ISSUE - INDEND INSIDE FOR LOOP
  print(b_list)

mutate([1,2,3,5,8,13])

#Debugging Odd or Even
# Which number do you want to check?
number = int(input())

if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")
  
# Error line 4: if number % 2 = 0:
# Remember that single "=" is assignment.
# Double "==" is checking for equality.