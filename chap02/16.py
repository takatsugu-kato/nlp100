import sys
import math
args = sys.argv
split = int(args[1])

path = "./hightemp.txt"
with open(path, "r", encoding="utf-8") as f:
    datas = f.readlines()

datas_len = len(datas)
unit = math.ceil(len(datas)/split)

for i, offset in enumerate(range(0, datas_len, unit), 1):
    with open("16_" + str(i) + ".txt", "w", encoding="utf-8") as out_file:
        for j in range(offset,offset+unit):
            out_file.writelines(datas[j])
