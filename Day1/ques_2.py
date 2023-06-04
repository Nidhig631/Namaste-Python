# 2- write a program which takes the name of the user as input and replace 
# all the occurence of character 'a' in the name to 'b' and print it.

name = input("enter your name")
print(f'old name {name}')
updated_name = name.replace('a','b')
print(f'new name {updated_name}')
