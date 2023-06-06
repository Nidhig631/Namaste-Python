# 1- write a program which takes single input from user
#  contaning first name,last name and age as 
# comma separated value and display then in 3 
# lines in given format below.

# example user input : Ankit,Bansal,35

# output:
# First name is Ankit
# last name is Bansal
# Ankit is 35 years old 

first_name,last_name,age = input("Enter the details").split()
print(f"First name is {first_name}")
print(f"last name is {last_name}")
print(f"Ankit is {age} years old ")