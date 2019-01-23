path = "./hightemp.txt"
with open(path, "r", encoding="utf-8") as f:
    datas = f.readlines()
print (len(datas))