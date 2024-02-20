# randomazation in python/ MODULES IN PYTHON (IMPORT- OS , RANDOM,BOTO 3)/ Methods in python -.APPEND,.LOWER,.INDEX ETC( TYPE LIST METHODS IN python)
# Ramdomisation can be used in - you VS computer game - ex: rock , paper, sisors,
# SEARCH FOR RANDOM modules in python
import random
a = random.randrange(1, 100)# actualy we have to g9ive 101 to print till 100
print (a) 
b= random.random()
print(b)
love_scroe = random.randint(1,10)
print(love_scroe)
#how to create our own module/create folder ownmodule and save- TO use it try IMPORT OWNMODULE
import day4_own_module
print(day4_own_module.a)
#Alternatively, you can use the from ... import ... syntax to import specific objects (functions, classes, variables) from your module:
from day4_own_module import greet
greet("Bob")
#This will directly import the greet() function from day4_own_module.py, 
# allowing you to call it without prefixing it with day4_own_modul.a


# head or tails random example
import random
random_side = random.randint(0, 1)# this is not range, we are giving direct value to randomize
if random_side == 1:
  print("Heads")
else:
  print("Tails")

# LIST - DATA STRUCTURE- JUST A WAY to organise & save data 
# tuple and list are same but we cant change values in tuple(immutable), ant it has normal bracket ()- to change tuple we have to typecast it as list
# to save sigle piece of data we have used variables
# list can have any type of date - string, float, boolean
hhhhh = ["ajay", 24,4.414,True,"nisha"]
print (hhhhh)
print (hhhhh[0])# to create list or to get item out of list we use [] squre bracket
print (hhhhh[2])
indian_states = ["tamilnau","kanada","goa","delhi"]
print (indian_states)
print (indian_states[3])# we get index error if its beyond delhi = print (indian_states[4])
indian_states[3]= "DELHIcapital"# we can change/alter like this
indian_states.append("ASSAM")# TO ADD AT END of the list/ you can find more in datastructure documentaion in python
print (indian_states)# dont need to memorise METHOD we have all in documentation
usa_states = ["Alabama","Alaska","California","New Jersey"]
world_states = [indian_states,usa_states]# its nested list
print(world_states)