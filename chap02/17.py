path = "./hightemp.txt"
cols1 = []
uniqs = set()
with open(path, "r", encoding="utf-8") as f:
    datas = f.readlines()
    for line in datas:
        cols = line.split("\t")
        if not(cols[0] in uniqs):
            uniqs.add(cols[0])

print (uniqs)