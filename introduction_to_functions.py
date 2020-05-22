#CodeAcademy
#May 22 2020

#INTRODUCTION TO FUNCTIONS
############################################

#8/11 Returns
#Create a function that calcualtes_age

def calculate_age(current_year, birth_year):
  age = current_year - birth_year
  return age

my_age = calculate_age(2049, 1993)
dads_age = calculate_age(2049,1953)

print("I am ", my_age, " years old and my dad is ", dads_age, " old.")



#9/11 Multipile Return Values
# Create a function with two return values

def get_boundaries(target, margin):
  low_limit = target - margin
  high_limit = margin + target
  return low_limit, high_limit

low, high = get_boundaries(100,20)
