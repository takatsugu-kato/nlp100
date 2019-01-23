path = "./hightemp.txt"
col1path = "col1.txt"
col2path = "./col2.txt"

cols1 = []
cols2 = []

def writecols (path,lines):
    with open(path, "w", encoding="utf-8") as f:
        f.writelines ("\n".join(lines))

with open(path, "r", encoding="utf-8") as f:
    datas = f.readlines()
    for line in datas:
        cols = line.split("\t")
        cols1.append(cols[0])
        cols2.append(cols[1])

writecols(col1path,cols1)
writecols(col2path,cols2)

