# Dictionaries & nesting
# dictionary are similar to real dictionary- all us to group together and tag related piece of infrmation
# every dictonary has - {key: value,key2: value2,etc}

fruites = {"banana": "100g","apple": "200g","mango": "500g",123: 1000}

print(fruites["mango"])# this is how we retrive data
print(fruites[123])
fruites[123] = 20000 # we can change or update inputs
print(fruites[123])
# creating empty dictionary- is simar to list in maximum all options
empty_dictionary = {}
#wipe a exixting dictionary
print(fruites)
fruites = {}
print(fruites)
fruites = {"banana": "100g","apple": "200g","mango": "500g",123: 1000}
#loop in dictonary will give only key, so we use additional print below
for char in fruites:
    print(char)#will give only key
    print(fruites[char])
# demo priject with dictonary
    student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Covert scores into grades.
for student in student_scores:
  score = student_scores[student]
  if score > 90:
    student_grades[student] = "Outstanding"
  elif score > 80:
    student_grades[student] = "Exceeds Expectations"
  elif score > 70:
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Fail"
    
print(student_grades)

# nesting - list or dictonaty

#Nesting a List in a Dictionary

travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting Dictionary in a Dictionary

travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

#Nesting Dictionaries in Lists

travel_log = [
{
  "country": "France", 
  "cities_visited": ["Paris", "Lille", "Dijon"], 
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]

#project for above
country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string
travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Your code here 👇
def add_new_country(name, times_visited, cities_visited):
  new_country = {}
  new_country["country"] = name
  new_country["visits"] = times_visited
  new_country["cities"] = cities_visited
  travel_log.append(new_country)

add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")

#- auction  secret bidding
