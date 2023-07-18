def reversed(sentence):
    words = sentence.split()
    print(words)
    reverse = [word[::-1] for word in words]
    reversed_string = "".join(reverse)
    return reversed_string



sentence = input("enter the sentence")
reversed_string = reversed(sentence)
print(reversed_string)