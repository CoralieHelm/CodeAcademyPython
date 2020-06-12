#June 11 2020
#CONTROL FLOW PRACTICE
#Relational Operators II
#Calvin Coolidge’s Cool College Practice
print("*****Welcome to Calvin Coolidge’s Cool College*****")
#Task 1. Write a function called greater_than that takes two integer inputs, x and y and returns the value that is greater. If x and y are equal, return the string
def greater_than(x,y):
  if x > y:
    return x
  if x < y:
    return y
  else:
    return "These numbers are the same"
#Task 2:
#The nearby college, Calvin Coolidge’s Cool College (or 4C, as the locals call it) requires students to earn 120 credits to graduate.
#Write a function called graduation_reqs that takes an input credits and checks if the student has enough credits to graduate. If they do, return the string
def graduation_reqs1(credits):
  if credits >= 120:
    return "You have enough credits to graduate!"
#Task 3:
print(graduation_reqs1(120))

#Task 4:
#Let’s return to Calvin Coolidge’s Cool College. 120 credits aren’t the only graduation requirement, you also need to have a GPA of 2.0 or higher. Rewrite the graduation_reqs function so it takes two inputs, gpa and credits, and checks to see if a student meets both requirements using an and statement.
#If they do, return the string
def graduation_reqs2(credits, gpa):
  if credits >= 120 and gpa >= 2.0:
    return "You meet the requirements to graduate!"
#Task 5:
#The registrars office at Calvin Coolidge’s Cool College has another request. They want to send out a mailer with information
#on the commencement ceremonies to students who have met at least one requirement for graduation (120 credits and 2.0 GPA).
#Write a function called graduation_mailer that takes two inputs, gpa and credits and
#checks if a student either has 120 or more credits or a GPA 2.0 or higher and if so returns True.
def graduation_mailer(gpa, credits):
  if gpa >=2.0 or credits >= 120:
    return True

#Task 6:
#The registrar’s office at Calvin Coolidge’s Cool College has been so impressed with your work so far that they have another task for you. They want you to return to the first function you wrote, graduation_reqs, and add in several checks using and and not statements.
#If a student meets both requirements the function should return
#"You meet the requirements to graduate!"
#If a student’s GPA is greater or equal to 2.0 but they don’t have enough credits the function should return
#"You do not have enough credits to graduate."
#If they have enough credits but their GPA is less than 2.0 the function should return
#"Your GPA is not high enough to graduate."
#If they do not have enough credits and their GPA is less than 2.0, the function should return
#"You do not meet either requirement to graduate!"
#Make sure your return value matches those strings exactly. Capitalization, punctuation, and spaces matter!
def graduation_reqs3(gpa, credits):
  if gpa >= 2.0 and credits >= 120:
    return "You meet the requirements to graduate!"
  elif gpa >= 2.0 and credits < 120:
    return "You do not have enough credits to graduate."
  elif gpa  < 2.0 and credits >= 120:
    return "Your GPA is not high enough to graduate."
  elif gpa < 2.0 and credits < 120:
    return "You do not meet either requirement to graduate!"

#Task 7:
#Calvin Coolidge’s Cool College has another request for you. They want you to add an additional check to the graduation_reqs function. If a student is failing to meet both graduation requirements, they want the function to return:
#"You do not meet the GPA or the credit requirement for graduation.
#Use an else statement to add this to your function.
def graduation_reqs(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"
  if (gpa >= 2.0) and not (credits >= 120):
    return "You do not have enough credits to graduate."
  if not (gpa >= 2.0) and (credits >= 120):
    return "Your GPA is not high enough to graduate."
  else:
      return "You do not meet the GPA or the credit requirement for graduation."

#Task 8:
#Calvin Coolidge’s Cool College has noticed that students prefer to get letter grades over GPA numbers. They want you to write a function called grade_converter that converts an inputted GPA into the appropriate letter grade. Your function should be named grade_converter, take the input gpa, and convert the following GPAs:
#4.0 or higher should return "A"
#3.0 or higher should return "B"
#2.0 or higher should return "C"
#1.0 or higher should return "D"
#0.0 or higher should return "F"
#You can do this by creating a variable called grade.
#Then, you should use elif statements to set grade to the appropriate letter grade for the gpa entered.
#At the end of the function, return grade.
def grade_converter(gpa):
  if gpa >= 4.0:
    grade = "A"
    return grade
  elif gpa >= 3.0:
    grade = "B"
    return grade
  elif gpa >= 2.0:
    grade = "C"
    return grade
  elif gpa >= 1.0:
    grade = "D"
    return grade
  else:
    grade = "F"
    return grade

#Task 9:
#The admissions office at Calvin Coolidge’s Cool College has heard about your programming prowess and wants to get a piece of it for themselves.
#They’ve been inundated with applications and need a way to automate the filtering process. They collect three pieces of information for each applicant:
#Their high school GPA, on a 0.0 - 4.0 scale.
#The number of extracurricular activities they participate in.
#The admissions office has a cutoff point for each category. They want students that have a GPA of 3.0 or higher, a personal statement with a score of 90 or higher, and who participated in 3 or more extracurricular activities.
#Write a function called applicant_selector which takes three inputs, gpa, ps_score, and ec_count. If the applicant meets the cutoff point for all three categories, have the function return the string:
def applicant_selector(gpa, ps_score, ec_count):
  if gpa >= 3.0 and ps_score >= 90 and ec_count >= 3.0:
    return "This applicant should be accepted."
  elif gpa >= 3.0 and ps_score >= 90 and ec_count < 3.0:
    return "This applicant should be given an in-person interview."
  else:
    return "This applicant should be rejected."

#My additional pratice:
print("To check if you pass the requirements, please enter the following information:")
student_gpa = input("Please, enter your GPA: ---> ")
student_credits = input("Kindly, enter your credits: ---> ")
student_ps_score = input("What is your PS Score: ---> ")
student_ec_count = input("What is the score of your Extracurricular Activities: ---> ")
