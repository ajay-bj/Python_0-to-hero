#LOOPS IN PYTHON
# simple For loop/ use for loop if u wantoo print out each items individualy one by one
fruits = ["apple","mango","banama","waterlemon"]
for eat in fruits:
    print(eat)
    print(eat+" pie")# give space inside" " - for apple_pie
# for loop has loop+variable = for eat in fruits:(FIRST LINE CODE- eat is variable which will be constantly changing with given input FRUITS & 2ND LINE CODE IS CONSIDERED AS LOOP EX:apple pie, then varible changes then loop, then variable chenges then loop )
#this 2ndline or 3rd line will be in loop when the are indended inside for loop, outside -for loop wont be looped


# pythone code for reversing a string without built in fuction
BAD_ass= "ajay"
reversed_string = ""
for char in BAD_ass:
   reversed_string = char + reversed_string # BOTH ARE SAME reversed_string += char
   print (reversed_string)

# Input a Python list of student heights - project handson
student_heights = input().split()# input to give in terminal- 146 138 127 167 185
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# Your code below this row 👇
print(len(student_heights))
total_height = 0
for height in student_heights:
  total_height += height
print(f"total height = {total_height}")

number_of_students = 0
for student in student_heights:
  number_of_students += 1
print(f"number of students = {number_of_students}")

average_height = round(total_height / number_of_students)
print(f"average height = {average_height}")

# TILL NOW WE HAVE ONLY SEEN FORLOOP WITH LIST
# NOW we SEE WITH RANGE + FORLOOPS
for number in range(1,10): # wont print 10, will stop to 9
   print(number)
for num in range(1,10,2):# steps by 2
   print(num)
total=0
for ajay in range(1,100):
   total += ajay
print(total)

# project even sum of number from 1 to 100
target = int(input()) # Number between 0 and 100
# Your code here 👇
even_sum = 0
for number in range(2, target + 1, 2):
  even_sum += number
print(even_sum)

# or

# alternative_sum = 0
# for number in range(1, target + 1):
#   if number % 2 == 0:
#     alternative_sum += number
# print(alternative_sum)

# fizz bus game - 1 to 100 foe xxample ,say 1,2,fizz(3),4,buzz(5)......divisible by 3 say FIZZ, div by 5 say BUZZ, both3&5 say FIZZBUZZ
target = 100
for number in range(1, target + 1):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level
# password = ""

# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password += random.choice(numbers)

# print(password)

#Hard Level
password_list = []

for char in range(1, nr_letters + 1): # WE DONT USE CHAR VARIABLE in output , just  looping purpous we use forloop with range 
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:# here we use both variable and loop to print password
  password += char

print(f"Your password is: {password}")