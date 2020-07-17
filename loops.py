#July 16 2020
#Introduction to Loops
#Break and Continue Exercise

#Example when a Break Statement is used. For example, iterating over a list until a certain condition is met. By using the break statement
#we avoid having to iterat over the complete list thereby saving memory and time.
dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'

for dog in dog_breeds_available_for_adoption:
  print(dog)
  if dog == dog_breed_I_want:
    print("They have the dog I want!")
    break

#Example when a Continue Statement is used. For example, when we’re iterating through lists, we may want to skip some values like negative values.

ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for age in ages:
  if age < 21:
    continue
  else:
    print(age)

#While loops can be useful when you don’t know how many iterations it will take to satisfy a condition. The while loop performs a set of code until some condition is reached.
all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

while len(students_in_poetry) < 6:
  student = all_students.pop()
  students_in_poetry.append(student)
  print(students_in_poetry)

#Nested Loops
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0


for location in sales_data:
  for scoop in location:
    scoops_sold += scoop
    print(location)

print(scoops_sold)

#List Comprehensions
can_ride_coaster = [height for height in heights if height > 161]
print(can_ride_coaster)

#We have provided a list of temperatures in celsius.
#Using a list comprehension, create a new list called fahrenheit that converts each element in the celsius list to fahrenheit.

celsius = [0, 10, 15, 32, -5, 27, 3]

fahrenheit = [(c * 9/5 + 32) for c in celsius ]
print(fahrenheit)

#Review
single_digits = range(10)
squares = []

for digit in single_digits:
  squares.append(digit**2)
  print(digit)

print(squares)

cubes = [digit ** 3 for digit in single_digits]
print(cubes)
