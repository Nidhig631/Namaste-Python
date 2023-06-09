# 9-  write a program that reverses a given string. 
# For example, if the input is "Hello" from user, the
#  output should be "olleH"

reverse_stng=""
String = input("Enter the string")
for i in range(len(String)):
    reverse_stng=String[::-1]
print(reverse_stng)
