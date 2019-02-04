import re
from nltk.stem.porter import PorterStemmer as PS

separater = [r"\.",";",":",r"\?","!"]
path = "./nlp.txt"

def parseLines (path):
    with open(path,"r",encoding="utf-8") as f:
        data = f.readlines()
    lines = []
    pattern = "(" + "|".join(separater)  + ") ([A-Z])"
    for line in data:
        line = line.strip()
        if (len(line)):
            result = re.sub(pattern, "\\1\n\\2", line)
            lines.extend(result.split("\n"))
    return lines

def splitWord (sentence):
    return line.split(" ")

def remove_symbple (word):
    result = re.sub(r"\W", "", word)
    return result

lines = parseLines(path)

ps = PS()
for line in lines:
    words = splitWord(line)
    for word in words:
        print (word + "\t" + ps.stem(remove_symbple(word)))
    print ("\n")