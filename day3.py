# WE WILL LEARN CONDITIONAL STATEMENT / LOGICAL OPERATOR/ CODE BLOCKS
 
# IF STSTEMENT- indendation and : is important / multiple if in succession
# Which year do you want to check?
year = int(input())

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")
  
# NESTED IF / ELSE 

print ("welcome to basket ball ground")
height = int(input("what is your height?"))
age    = int(input("what is your age?"))
if height >= 100:
    print("tall")
    if age >= 10:
        print("you are tall with correct age- allowed to play")
    else:
        print ("cant play")
elif height > 80:
    print("medium")
elif height > 80:
    print("medium")
elif height > 50:
    print("average")
elif height == 10:
    print("average")
else:
    print ("shot")

# logical operator = toinclude many condition in same like of code
    # if condition1 & condition2 & condition 3- and / or / not
    # a and b- both must be true- to get entire line true
    # a or b - any one must be true - to get entire line true
    # not b (False) - it reverses like if true- then its false/ if false - then its true 
    #ASCII Character Codes: buffolow/ tiger / rino etc / aws amazon 2 ami image


print("The Love Calculator is calculating your score...")
name1 = input()  # What is your name?
name2 = input()  # What is their name?
# Your code below this line 👇
combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))
if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
