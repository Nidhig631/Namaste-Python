# 7- write a python function that accepts a
#  string and prints the count of occurence of each characters
# sample string: aabccda
# expected result:
# a -> 3
# b-> 1
# c-> 2
# d -> 1


def count_characters(string):
    character_count = {}

    for char in string:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1

    for char, count in character_count.items():
        print(char, "->", count)

# Example usage
input_string = input("Enter a string: ")
count_characters(input_string)