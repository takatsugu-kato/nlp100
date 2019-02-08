import tarfile
import numpy as np
import re

def addLabel(path,polarity):
    ti = tf.getmember(path)
    f = tf.extractfile(ti)
    data = f.readlines()
    results = []
    for line in data:
        results.append(polarity + " " + line.decode("windows-1252"))
    return results

with tarfile.open("./rt-polaritydata.tar.gz","r",encoding="utf8") as tf:
    negs = addLabel("rt-polaritydata/rt-polarity.neg","-1")
    poss = addLabel("rt-polaritydata/rt-polarity.pos","+1")

concatenate = np.concatenate([negs, poss], axis=0)
np.random.shuffle(concatenate)

with open("./sentiment.txt", "w", encoding="utf-8") as out_file:
    out_file.writelines(concatenate)

with open("./sentiment.txt", "r" , encoding="utf-8") as f:
    data = f.readlines()
    neg = [line for line in data if line.startswith("-1")]
    pos = [line for line in data if line.startswith("+1")]

    print (len(neg))
    print (len(pos))