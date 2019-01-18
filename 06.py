def ngram(string, n):
    result = set()
    for i in range(0,len(string)-n+1):
        result.add(string[i:i+n])
    return result

string1 = "paraparaparadise"
string2 = "paragraph"

X = ngram(string1,2)
Y = ngram(string2,2)

print (X)
print (Y)

union = X | Y
print (union)

intersection = X & Y
print (intersection)

difference = X - Y
print (difference)

print('seがXに含まれる:' + str('se' in X))
print('seがYに含まれる:' + str('se' in Y))