import collections
path = "./hightemp.txt"
kens = []
with open(path, "r", encoding="utf-8") as f:
    datas = f.readlines()
    for line in datas:
        splitted_line = line.split("\t")
        kens.append(splitted_line[0])

c = collections.Counter(kens)

for data in (c.most_common()):
    print (data)