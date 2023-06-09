# 7- consider the below list of list conatins following information :

# 1. The name of a university 
# 2. The total number of enrolled students
# 3. The annual tuition fees
# write a program to print follwoing information :
# 1- a list of all the universitites  : ['California Institute of Technology','Harvard',..so on]
# 2- total number of student entrolled in all the unversities together 
# 3- mean of tuition fees


uni_info = [
    ['AKTU',32,78888],['GLA',34,834567],
    ['LPU',23,98777],['ALU',12,876545]
]
#1
# list_unv=[]
# for i in uni_info:
#     list_unv.append(i[0])
# print(list_unv)   

#2
# 2- total number of student entrolled in all the unversities together 


# stu_list_count=[]
# for i in uni_info:
#     stu_list_count.append(i[1])
# a=sum(stu_list_count)
# print(a)    

#3- mean of tuition fees
stu_list_count=[]
for i in uni_info:
    stu_list_count.append(i[1])
a=sum(stu_list_count)/len(stu_list_count)
print(a)   