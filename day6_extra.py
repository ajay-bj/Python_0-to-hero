# input function in function
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def multi(n1, n2):
    return n1 * n2

def div (n1, n2):
    return n1 / n2

# this is higher order function
def calculator(n1, n2, func): # we give function inside functin
    return func(n1, n2) # have to define that in paranthesis ()

print(calculator(2,3, add)) # we have called function with functionas input