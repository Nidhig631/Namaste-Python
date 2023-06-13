# 5- Write a Python function that checks whether a passed string
#  is a palindrome or not.
# Note: A palindrome is a word, phrase, or sequence that 
# reads the same backward as forward, e.g., madam.

def pandil(words_str):
    reversed_strg = words_str[::-1]
    return words_str == reversed_strg

words_str = input("Enter the string")
pandil(words_str)
if pandil(words_str):
    print("Panlindrome")
else:
    print("not")    