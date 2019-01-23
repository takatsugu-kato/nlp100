import sys
args = sys.argv
end_row = int(args[1])
path = "./hightemp.txt"
with open(path, "r", encoding="utf-8") as f:
    datas = f.readlines()
    for i in range(0, end_row):
        print(datas[i])