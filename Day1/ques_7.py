# 7- take 3 inputs from user : first name , last name and age . Display the information in below format
# exmaple 
# first name : MOhit
# last name : sharma 
# age 32
# Display : my name is Mohit Sharma and I am 32 years old.
# note that first letter of first name and last name both should be in capital letters and rest in small. 

first_name = input("Enter the first_name").lower().title()
last_name = input("Enter the last_name").lower().title()
age = input("Enter the age")
print(f'my name is {first_name} {last_name} and I am {age} years old ')