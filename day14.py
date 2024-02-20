# OWN class,object, attribute creation in python( PascalCase/ snake_case/ camelCase)

# to create class we have to use class keyword followed by Class: ( Pascal Case- EVERY STARTING WORD OF CLASS MUST BE CAPITAL)
# class User:
#     pass# is helps to declar empty by letting to pass next line

# user_1 = User() # have created object from class
# user_1.id = "121"# have create attributes
# user_1.username = "ajay"# have create attributes

# print(user_1.username)

# # every time its difficult to create user again anad again - can lead to typo error
# user_2 = User() # have created object from class
# user_2.id = "333"# have create attributes
# user_2.username = "nisha"# have create attributes

# print(user_2.username)
# to resolve this we have CONSTRUCTOR- this is called initialize an object
# to create we use special function _ _init_ _

class Car:

    def __init__(self,seats):
        self.seats = seats # this is how to set attributes

my_car = Car(5)     # this is exactly same as we creates attribute above user_1.id = "121"/ or my_car.seats = 5
print(my_car.seats)   

class User:

    def __init__(self, user_id, username):# when you add parameters to the constructor- it means when ever a new object been construsted from this class it must provide this 2 pieces of data
        self.user_id = user_id
        self.username = username
        self.followers = 0  # we can provide even default value
        self.following = 0

    def follow(self,user): # this is how adding methods to a class, methon unlike a function must have self as first parameter
        user.followers += 1 # when called self helps in identifing object which called it
        self.following += 1

        
user_1 = User("111","AJAY")
user_2 = User("222","nisha")
    
print(user_1.user_id)
print(user_1.username)
print(user_1.followers)

user_1.follow(user_2)# we are caling a method
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

################################################################################

# Classes:
# In OOP, a class is a blueprint for creating objects. Objects are instances of a class, and they encapsulate data and behavior

class AWSInstance:
    def __init__(self, instance_id, instance_type, region):
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.region = region
        self.status = 'stopped'

    def start_instance(self):
        print(f"Starting instance {self.instance_id} in region {self.region}.")
        # Code to interact with AWS SDK to start the instance
        self.status = 'running'

    def stop_instance(self):
        print(f"Stopping instance {self.instance_id} in region {self.region}.")
        # Code to interact with AWS SDK to stop the instance
        self.status = 'stopped'
# In this example, the AWSInstance class has three attributes (instance_id, instance_type, region) and two methods (start_instance and stop_instance).

# Attributes:
# Attributes are variables that store data. In our example, instance_id, instance_type, region, and status are attributes.

# Methods:
# Methods are functions that operate on the data of the object. The start_instance and stop_instance methods are actions that can be performed on an AWSInstance object.

# Now, let's create instances of the AWSInstance class and use its methods:


# Creating instances
instance1 = AWSInstance(instance_id='i-12345', instance_type='t2.micro', region='us-east-1')
instance2 = AWSInstance(instance_id='i-67890', instance_type='m5.large', region='us-west-2')

# Accessing attributes
print(f"Instance 1 ID: {instance1.instance_id}")
print(f"Instance 2 Type: {instance2.instance_type}")

# Using methods
instance1.start_instance()
instance2.stop_instance()

# Accessing updated attributes
print(f"Instance 1 Status: {instance1.status}")
print(f"Instance 2 Status: {instance2.status}")
# In this example, we create two instances of AWSInstance and perform actions on them using the defined methods.

# This is a basic introduction to OOP in Python. In real-world scenarios, you might have more complex class hierarchies, inheritance, and polymorphism to model your system effectively.
# The idea is to structure your code in a way that mirrors the real-world entities and their interactions


# what is self

# ChatGPT
# In Python, self is a conventional name for the first parameter of a method within a class. It represents the instance of the class that the method is associated with. When you call a method on an object, the object itself is automatically passed as the first parameter to the method.

# For example:

class MyClass:
    def __init__(self, value):
        self.value = value

    def print_value(self):
        print(self.value)

# Creating an instance of MyClass
obj = MyClass(value=42)

# Calling a method on the instance
obj.print_value()

# In this example, self refers to the instance of MyClass. When you call obj.print_value(), self inside the print_value method will be obj, and it can access the value attribute of that specific instance.

# It's important to note that self is just a convention; you could technically use any name for the first parameter of a method. However, using self is widely accepted and makes the code more readable and consistent with Python conventions.