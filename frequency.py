def frequency(sentence):
    words=sentence.replace(".", "").split(" ")
    frequency_word={}

    for word in words:
        if word in frequency_word:
            frequency_word[word] += 1
        else:
            frequency_word[word]=1
        
    return frequency_word


sentence = "This is a test sentence. This sentence is a test."
result = frequency(sentence)
print(result)