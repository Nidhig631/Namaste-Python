# 10- Write a function called capitalize_odd_letters
#  that takes a string as input and returns the same 
# string with the odd-indexed letters capitalized.
def capitalize_odd_letters(string):
    capitalized_string = ""

    for i in range(len(string)):
        if i % 2 == 1:  # Check if the index is odd
            capitalized_string += string[i].upper()
        else:
            capitalized_string += string[i]

    return capitalized_string

# Example usage
input_string = input("Enter a string: ")
result = capitalize_odd_letters(input_string)
print("Modified string:", result)
