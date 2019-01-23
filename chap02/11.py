path = "./hightemp.txt"
with open(path, "r", encoding="utf-8") as f:
    datas = f.readlines()
    for line in datas:
        print(line.replace("\t"," "), end="")