# def greet():
#     print("Good Morning")

# greet()    

# def sum(a,b=1):
#     c=a+b
#     return c

# d= sum(3) # if  we do not pass it will take defualt value
# print(d)


# num =4
# def getsum(a,b=1):
#     num =a+b
#     return num

# d = getsum(1,5)
# print(d)
# print(num)

# def  getsum(a,b):
#     print(a,b)

# d = getsum(b=1, a=2)
# print(d)

# for any number of arguments using tuple
# def getsum(*args):
#     print(args,type(args))
#     num=0
#     for a in args:
#         num = num+a
#     return num

# d= getsum(1,2,3)
# print(d)    

#for any number of karguments as dic
# def getsum(**kargs):
#     print(kargs,type(kargs))

# d= getsum(id=24,name='Nidhi',age=34)
# print(d)    
# def getsum(a,b):
#     print(a,type(a))

# d= getsum(b=1,a=2)
# print(d)    

import calc
print(calc.getsum(1,2))