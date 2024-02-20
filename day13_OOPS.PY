# OOPS VS PROCEDURAL PROGRAMING(old way) , adding python  packages(pypi)

# splitting complex tasks into seperate module- ex self driving car making by group of people handeling each = productivity, quick, easy, reusable
# oop ex- 1person restarunt(japan) vs 4people restraunt handeling, with each assigned roles
# it mimicks the real world examples so its called oop, ex- waiter, chef, cleaner, manager
# ex- waiter has 2 - attribute(variable for waiter) & methods(functios of waiter)


# CONSTRUCTING NEW OBJECT- OBJECT = CLASS
import turtle # or import turtle as t - instead of writing turtle every time we can use t
nisha = turtle.Turtle() # instead of writing turtle every time we can use t- nisha = t.Turtle()
print(nisha)
# or 
from turtle import Turtle # or we use * for everything import- from turtle import */ or 
pingu = Turtle()          
print(pingu)
pingu.shape("turtle")# we called tuttle name(object.method) pingu.shape and changed its shape
pingu.color("red", "green")
pingu.forward(100)# to move forward
# WHAT DO WE DO WITH OBJECTS- CALL IT BY object.attribute / 
# line 21 object.methods( its function so no need print)
# now we have changed the shapein line 16 with (object.method)

my_screen = turtle.Screen()# CREATING OBJECT
my_screen.canvheight = 1000 # this is how we change attributes( default was 300)
print(my_screen.canvheight)# object.attribute
my_screen.exitonclick()# object.methods( exitonclick screen wil poopof, of the turtle)


