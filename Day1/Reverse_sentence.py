def reversed_words(sentence):
    words = sentence.split()
    print(words)
    rev_words = [word[::-1] for word in words]
    print(rev_words)
    reversed_sentence = "".join(rev_words)
    return reversed_sentence
        


sentence = input("Enter the sentence")
reversed_sentence = reversed_words(sentence)
print(f'reversed_sentence: {reversed_sentence}')