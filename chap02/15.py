import sys
args = sys.argv
rows = int(args[1])
path = "./hightemp.txt"
with open(path, "r", encoding="utf-8") as f:
    datas = f.readlines()
    for i in range(len(datas) - rows, len(datas)):
        print(datas[i].replace("\n",""))