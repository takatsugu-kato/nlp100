import re

string = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
words = string.split(" ")
alphabet_count = []
for word in words:
    alphabet_count.append(len(re.findall('[a-zA-Z]', word)))

print (alphabet_count)