#we will learn- datatype/ number/operation/ F STRING
#string examples
print(len("ajaynisha"))# it will be 9
print("ajaynisha"[8])#for range it counted from o to 8

#integer- is a wholenumber
print("100"+"100")# is a string
print(100 +100) # now its integer

#float is for floatingpoint number
3.414

#boolean only has true or false
True
False
len("ajay")#only works with string not int/ use type
print(type(len))
#typecasting- changing data type from one to another
print(len(str(4564567890)))

#mathhematical operatin
3+5
print (3 + 5)
print (3 - 5)
print (3 * 5)
print (6 / 2)#we get float
print (int(6 / 2))#type casted and changed as integer
print ( 2 ** 3)# this is exponential = power- 2 power3=8
print((1.5*2.5))
print(round(1.5*2.5))# ROUND FUNCTION
print(round(1.53333333334*2.544434343434,4))# SETING 4DIGITS TO BE ROUND
score = 4
a = (score  + 1)
print (a)
# += is effective
score *= 2
print (score)
score /= 2
print (score)
score -= 1
print (score)

# TO ADD DIFFERENT VARIABLE WITH DIFFERENT DATA TYPE IN STRING - F STRING
score = 100
height = 2.555555555
result_we_won = True
print(f"we wone {result_we_won} with {score} ball hight{height}")
