# 9- write a function called generate_fibonacci that 
# takes an integer n as input and returns a list of the
# first n Fibonacci numbers.

def generate_fibonacci(n):
    fibonacci_sequence = []

    if n >= 1:
        fibonacci_sequence.append(0)
    if n >= 2:
        fibonacci_sequence.append(1)

    for i in range(2, n):
        fibonacci_sequence.append(fibonacci_sequence[i-1] + fibonacci_sequence[i-2])

    return fibonacci_sequence

# Example usage
input_n = int(input("Enter a number: "))
fibonacci_numbers = generate_fibonacci(input_n)
print("Fibonacci sequence:", fibonacci_numbers)
