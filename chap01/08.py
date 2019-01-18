def cipher(string):
    result = ""
    for c in string:
        if c.islower():
            result += chr(219-ord(c))
        else:
            result += c
    return result

string = "pYthon iS a gooD proGramming laNguage"

print (cipher(string))

print (cipher(cipher(string)))