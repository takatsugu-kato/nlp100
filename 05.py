
def ngram(string, n):
    # print (words)
    result = []
    for i in range(0,len(string)-n+1):
        result.append(string[i:i+n])
    # print ([tuple(string[i:i+n]) for i in range(len(words)-n+1)])
    return result

string = "I am an NLPer"

#単語bi-gram
words = string.split(' ')
result = ngram(words, 1)
print (result)
#文字bi-gram
result = ngram(string, 1)
print (result)
