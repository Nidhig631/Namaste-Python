# 3- Write a Python function that accepts a string
#  and counts the number of upper and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

def count_lower_upper(sentence):
    upper_count =0
    lower_count=0
    for word in sentence:
        if word.isupper():
            upper_count = upper_count+1
        else:
            lower_count = lower_count +1
    return upper_count,lower_count

sentence = 'The quick Brow Fox'
upper, lower = count_lower_upper(sentence)
print("upper count is ",upper)
print("lpper count is ",lower)