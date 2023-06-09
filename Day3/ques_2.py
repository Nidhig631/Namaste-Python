# 2- given a list of numbers unsorted, write a program to find the median
#  of the numbers in list

list =[11,0,9,5,6]
list.sort()
print(list)
number =  len(list) 
if number%2==0: 
    print(number)
    median = (list[number//2 -1] + list[number//2])/2
    print(f'median is: {median}')
else:
    median = list[number//2]
    print(f'median is: {median}')