import tarfile
import numpy as np
import nlp71
from nltk.stem.porter import PorterStemmer as PS
import re
import collections

def remove_symbple (word):
    result = re.sub(r"\W", "", word)
    return result

ps = PS()
words = []
with open("./sentiment.txt","r",encoding="utf-8") as f:
    data = f.readlines()
    for line in data:
        for word in line[3:].split(' '):
            stem = ps.stem(word)
            stem = remove_symbple(stem)
            if not nlp71.isStopWord(stem) and not stem == "":
                words.append(stem)

c = collections.Counter(words)

with open ("./features.txt","w",encoding="utf-8") as out_file:
    for data in c.keys():
        if c[data] >= 6:
            print (data + ": " + str(c[data]))
            out_file.writelines(data + "\n")
