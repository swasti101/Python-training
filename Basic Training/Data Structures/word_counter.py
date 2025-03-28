def word_counter(sentence):
    words = sentence.split()
    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1
    
    return freq

s1 = "hello hello hi hello"
print(word_counter(s1))