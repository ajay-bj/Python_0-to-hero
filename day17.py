# list and dictonary comprehension - helps to cut down lots of code 
# its unique to python

# how to create list using list comprehension
# creating new list from prvious list
nubmer = [1,2,3]
new_list = []
for aj in nubmer:
    add_to = aj + 1
    new_list.append(add_to)
print(new_list)
new_list = [] # is done to execute below code as new
# list comprehension-> new_list = [new_item(expression) for item(aj) in list(original list -number)]
new_list = [aj + 1 for aj in nubmer]
print(new_list)

name = "ajay balaji"
new2_list = [letter for letter in name]
print(new2_list)

range_list = [ran * 2  for ran in range(1,11) ]
print(range_list)

# conditional list comprehension-> new_list = [new_item for item in list if test] this only works if iftest is true
names_list = ["ajay","nisha","anitha","rathu","ravi"]
short_name = [short.upper() for short in names_list if len(names_list) > 3]
print(short_name)

# data overlap project- file1&2 contains numbers like 3,4,55,67,45,etc
# with open("file1.txt") as file1:
#   list1 = file1.readlines()
    
# with open("file2.txt") as file2:
#   list2 = file2.readlines()
    
# result = [int(num) for num in list1 if num in list2]

# # Your code above 👆
# print(result)

# DICTONARY COMPREHENSION-> new_dict = {newkey:newvalue for item in list(range or string)}
#-> new_dict = {newkey:newvalue for (key, value) in dict.item() if test}
# assigining values to list to have dictonary 
name = ["ajay","nisha","anitha","rathu","ravi"]
import random
students_score = {student:random.randint(1,100) for student in name}
print(students_score)

passed_students = {students: score for (students, score) in students_score.items() if score >= 60}
print(passed_students)