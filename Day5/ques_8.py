# 8- write a function called is_prime that takes an integer as 
# an argument and returns True if it is a prime number, and
# False otherwise.

#Enter   number 
def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    return True

# Example usage
input_number = int(input("Enter a number: "))
if is_prime(input_number):
    print("The number is prime.")
else:
    print("The number is not prime.")




# 11- write a function called find_common_elements that takes two lists as input and returns a new list containing the common elements between the two lists.

