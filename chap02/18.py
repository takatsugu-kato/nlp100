from operator import itemgetter
path = "./hightemp.txt"
lists = []
with open(path, "r", encoding="utf-8") as f:
    datas = f.readlines()
    for line in datas:
        splitted_line = line.split("\t")
        lists.append(splitted_line)

lists.sort(key=itemgetter(2), reverse=True)

for line in lists:
    print (line)