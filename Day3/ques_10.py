# out=[]
# out1=[]
# x = [['id',1,0],['id',1,2],[['s',9]]]
# for i in x:
#         out = out + i
# # print(out) 
# for j in out:
#         if isinstance(j,list):
#             out1 = out1 + j
#         else:
#             out1.append(j)    
# print(out1) 

# x10- write a program that finds the largest number in a 
# list(unsorted) of integers without using sort/sorted method.

list = [9,100,51,32,2]
largest_nuber = list[0]
for i in list:
     if i > largest_nuber:
        largest_nuber=i
print(largest_nuber)