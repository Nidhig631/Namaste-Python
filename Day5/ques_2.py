
# 2- write a Python function which takes a positive number 
# as input and return the factorial of the number.

def fac(n):
    r=1
    if n  < 0:
        print("Enter the +ve positive numbers -ve are not allowed.")
    elif n==0 :
        print("Factorial of number is 1")
    else:
        for i in range(2,n+1):
            r = r * i 
        return r

n = fac(5) 
print(n)