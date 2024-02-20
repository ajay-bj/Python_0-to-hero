#functions with output- we have already seen functions with inputs
# we learnT RETURN , DOCSTRING , recursion- the function calls itself, we have used in calculator project
# print vs return - 
def formate_name(f_name, l_name): # change our input into Ajay Balaji-tittle case
    print(f_name.title())# .title() helps to convert as tittle case
    print(l_name.title())
formate_name("niSHA", "RAVI")
# VERSION2 , if reture is blank - then it will give none as output
def formate_name(f_name, l_name): # change our input into Ajay Balaji-tittle case
    variable_a = f_name.title() # .title() helps to convert as tittle case
    variable_b = l_name.title()
    print(f"{variable_a} {variable_b}")
    return f"{variable_a} & {variable_b}" # RETUR'S output replaces the part of code when function was called function( replaces the function itself)
                                          # so we have to use print with function call to print return
print(formate_name("AJay", "balaJI"))     # its same as output = len("ajaybalaji")- counts and stores as len then returns the value to output variable

# function with multiple return, after return no code works, it stops at return
# DOCSTRING is for function_documentation purpous- it has to go after first line of decleration with """ hi """
def format_name(f_name, l_name):
  """Documentation - title case conversion
   code,keep cursor on functioncall - 
    you will see this documentation """
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs."
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"Result: {formated_f_name} {formated_l_name}"

print(format_name(input("whats your firstname? "),
input("whats your last name? ")))