# 5- write a program which takes the name of the user as input and print the index of character 'a'
#  in the string. if 'a' is not there then return -1.

name = input("Enter the name: ")
find_a = name.lower().find('a')
print('index of "a"' , find_a)