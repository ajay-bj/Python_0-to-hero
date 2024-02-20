# FUNCTIONS , WHILE LOOPS , CODE BLOCKS, Importance of INDENDATION IN CODE
# LEN() , INT() , RANDOM(), INPUT(), RANGE() ,PRINT(),- ALL ARE BUILTIN FUNCTIONS
# TO CREATE OWN FUNCTION we have to define as - def <name of function():>
def own_function():
    print("wow your first function")
    print("thats great keep going")
#now we have to call our functon & and give input in () parantheses if needed
own_function()# calling our function just by its name & set of paranthesis

# CUT down a code we use FUNCTIONS, 2 LINES OF CODE INSTEAD OF 6 LINES & LOT MORE READABLE CODE 
# 2WAYS to indendation  SPACES VS TABS -STILL   DEBATES IS GONG ON STILL( OFFICIAL PYTHON USE SPACE)

# WHILE LOOP WORKS DIFFRENTLY THAN FORLOOP
#SYNTAX ----------> WHILE SWOMETHING_IS_TRUE: IT WILLGOINSIDE LOOP IN NEXT STEP( BASED ON TRUE AND FALSE CONDITION)

AJAY = 6
while AJAY > 0: # for not equal to ---> != can be used or use not command
    print(f"STILL IN LOOP {AJAY}")
    AJAY -= 1 # this continiously reduces ajay = ajay - 1 so att last zero so while becomes false so loop stops

# for not equal to ---> != can be used or use not command
nisha = False 
while not nisha : # we can insert if else inside while loop for solutions
    print(f"STILL IN LOOP {nisha}")
    for char in range(0,3):
        print("iam inside for loop")
        nisha = True

# for loops VS while loops - interview prepare
# robo in infinite loop - we have to debug for all kind of randiom situation robo stands
        
