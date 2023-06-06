# >>> 5/2
# 2.5
# >>> 5//2
# 2
# >>> 5%2
# 1
# >>> 6//2
# 3
# >>> 9//2
# 4
# >>> round(2.67)
# 3
# >>> 5.5 // 2.2
# 2.0
# >>> round(2.67,1)
# 2.7
# >>> round(2.67)
# 3
# >>> round(2.672,2)
# 2.67
# >>> 3%2
# 1
# >>> 12%2
# 0
# >>> abs(40
# ... )
# 40
# >>> abs(-1)
# 1
# >>> abs(-3)
# 3
# >>> 2**2
# 4
# >>> pow(2,2
# ... )
# 4
# >>> pow(2,3)
# 8
# >>> 2^3
# 1
# >>> pow(2,4,2)
# 0
# >>> a=2.0
# >>> a.is_integer()
# True
#Data structures
#List
#Tuple
#dict
#set
#LIST:-list is mutable,include different data type,

# print(type(ipl))
# #indexing
# print(ipl[0])
# print(ipl[-1])
#slicing
# print(ipl[0:3])
# ipl[1]='KKR'
# ipl[3]='MI'
# ipl.append('KKR')#add ele at the last
# ipl.insert(5,'KKKL')#add ele at the specific
# ipl.extend([1,2]) #pass list in extend and extend list with another list
# ipl = ['CSK','MI','RCB','LSK']
# ipl.insert(1,[3,4])
# print(ipl)
# print(ipl[0][0:2]) #one index ele two words

# method 1 to create list
# ipl_string1 = "CSK, I, KKR, LSG"
# ipl_string2 = "CSK I KKR LSG"
# ipl_string3 = "CS,|I,|KKR,|LSG"
# ipl_list1 = ipl_string1.split(",")
# ipl_list2 = ipl_string2.split(" ")
# ipl_list3 = ipl_string3.split(",|")
# print(ipl_list1)
# print(ipl_list2)
# print(ipl_list3)

# method 2 to create list
# python_list = list('python is love')
# for i in range(len(python_list)):
#     m = " ".join(python_list[::-1])
# print(m)

#method 3 
# python_list = list('Python')
# print(python_list)


#remove elements
#pop :- removes last element
# ipl = ['CSK','MI','RCB','LSK']
# print(ipl.pop())
# print(ipl)
# print(ipl.pop(1))
# print(ipl)

# num = [1,2,3,4,5]
# print(sum(num))
# print(max(num))
# print(num.pop(1))
# print(num)


# num = ['A','B','E','D','C']
# num1 = ['A','1','112','13','4','5']
# num1.sort()
# # print(num1)
# num1.index('A')
# # print(num)
# num1.index('A')
# print(num1.index('A'))
# a='A' in num1
# print(a)
# n = num1.sort()
# print(n)
# print(max(num))


list_of_list = [[1,2],[2,4],['Ankit','Rahul']]
# print(list_of_list[0])
# print(list_of_list[0][0])
# new_list_of_list = list_of_list
# print(list_of_list)
# print(new_list_of_list)
# new_list_of_list.pop()
# print(list_of_list)
# print(new_list_of_list)

# to avoid above issue change on same
copy_list_of_list = list_of_list.copy()
list_of_list.pop()
print(list_of_list)
print(copy_list_of_list)

#shallow copy and deep copy

copy_list_of_list = list_of_list.deepcopy()
list_of_list.pop()
print(list_of_list)
print(copy_list_of_list)
# 1) shallow copy: 