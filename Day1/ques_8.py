# 8- take 3 inputs from user : first name , last name and company name. create the email alias 
# for the user and display it.  Email alias is first 2 letters of first name , last 3 letters 
# of last name and @company.com
# example 
# first name : MOhit
# last name : sharma 
# company : infosys

# Display : morma@infosys.com 

# note full email id should -be in lower case



first_name = input("Enter the first_name ").lower().title()
last_name = input("Enter the last_name ").lower().title()
email = first_name[0:2] + last_name[0:3] + "@airtel.com"
print(email.lower())



