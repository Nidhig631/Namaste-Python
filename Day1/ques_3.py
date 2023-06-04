# 3- write a program which takes 2 inputs from user as principle amount (int) and rate of annual
# interest (float) 
# and print the expected total amount  after  2 years.

# example : principle : 100 , interest percent 10  then amount after 2 years will be : 100*1.1*1.1 = 121

PA = int(input("Enter the principal amount:"))
RAI = float(input("Enter the rate of annual interest"))
TA_after_2years = PA * (1 + (RAI / 100)) ** 2
print(f'expected total amount  after  2 years{int(TA_after_2years)}')