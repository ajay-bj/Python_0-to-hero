# FUNCTIONS WITH INPUTS /PARAMETERS(name of the data) & ARGUMENTS(actual data) 
def my_function(something):# something = 123 or ajay
    print(something)       #     |             |
                        #is parameter  / is argument
    print(f"helo \n \n {something}")

my_function(123)
my_function("ajay")

#functions with morethan 1 input
def personal_details (name, location, age, gender):
    print(f"welcome {name}")
    print(f"we know you are from {location}")
    print(f"you are {age}years of experienced {gender}")

personal_details("balaji","chennai",27,"male")# this is called POSITIONAL ARGUMENT ie:1st parameter takes 1st argument as input and so on
# to soleve this we have KEY WORD ARGUMENT 

def number (a,b,c,d):
    print(a,b,c,d)

number(3,2,4,1)#POSITIONAL ARGUMENT
number(1,2,3,4)#POSITIONAL ARGUMENT
number(a=1,c=3,b=2,d=4)#KEYWORD  argument even 1324 oder as argument it will take as per as assigned 

# PAINT AREA CALCULATOR priject
import math

def paint_calc(height, width, cover):
  num_cans = (height * width) / cover
  round_up_cans = math.ceil(num_cans)
  print(f"You'll need {round_up_cans} cans of paint.")


# Your code above this line 👆
test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

# prime number check project
def prime_checker(number):
  is_prime = True
  for i in range(2, number):
    if number % i == 0:
      is_prime = False
  if is_prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")   
# Your code above this line 👆
n = int(input()) # Check this number
prime_checker(number=n)


# CEASER ENCODE/DECODE PROJECT
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
      shift_amount *= -1
  for letter in start_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    end_text += alphabet[new_position]
  print(f"Here's the {direction}d result: {end_text}")


#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

