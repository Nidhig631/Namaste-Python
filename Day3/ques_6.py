# 6- write a program to take a positive number as input 
# from user. if the user enters negative number then keep 
# promting him to enter positive number until he enters the
# positive number and then print the same

# Prompt the user to enter a positive number
number = int(input("Enter a positive number: "))

# Keep prompting until a positive number is entered
while number <= 0:
    print("Invalid input. Please enter a positive number.")
    number = int(input("Enter a positive number: "))

# Print the positive number
print("The positive number you entered is:", number)
