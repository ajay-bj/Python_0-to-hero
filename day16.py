# open, read write a file &  mail merging & CSV file reading
# creating  a file.txt for handson purpous 
import os
print(os.getcwd())

file_path = r"C:\Users\anith\Desktop\vs\python100days\day16_myfile.txt" #You can prefix the string with r to create a raw string, which ignores escape characters.
aj = open(file_path)
print(aj.read())
aj.close()

print("lets us use with:-------> ")
# no need to remember close - so we use WITH
with open(r"C:\Users\anith\Desktop\vs\python100days\day16_myfile.txt") as aj:
    print(aj.read())# can delete close, aftre as is the variable which stores, 

with open(r"C:\Users\anith\Desktop\vs\python100days\day16_myfile.txt",mode="w" ) as nisha:
     nisha.write(" we have used write operation")
     # "a"- for append can use\n, 
     
##########################################################
#mail merging projext

# reading csv file
import csv # learn more in pandas documentation
import pandas # data analysis liberary/ as soon as csv file - use pandas

with open(r"C:\Users\anith\Desktop\vs\python100days\weather_data.csv") as datafile:
     #print(datafile.read())
     #print(csv.reader(datafile))
     data = csv.reader(datafile)
     for row in data:
          print(row)

analys = pandas.read_csv(r"C:\Users\anith\Desktop\vs\python100days\weather_data.csv")
print(analys)
print(analys["temp"])
print(type(analys)) # dataframe - structure 2 dimentional - we can convert to dictonary, html,etc
print(type(analys["temp"])) # series - one diment9ional - can conveer to list , check documuntation for more