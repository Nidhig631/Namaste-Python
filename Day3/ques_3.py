# 3- from a list of numbers create 2 list ,
#  one containing only the even numbers and other only the odd numbers

list = [0,1,2,3,4,5,6]
list_odd=[]
list_even=[]
for i in range(len(list)):
    if list[i]%2==0:
       list_even.append(i)
    else:
        list_odd.append(i)
print("odd elements are",list_odd)
print("even elements are ",list_even)