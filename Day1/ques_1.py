# 1- write a program which takes 2 inputs from the user : weight(kg) and height(meter) and prints the BMI in the output.

# BMI = weight / (square of height)
# number ** exponent
weight = int(input("Enter the weight value:"))
height = int(input("Enter the height value:"))
BMI = weight / (height ** 2)
print(f'calculated BMI is:{BMI}')