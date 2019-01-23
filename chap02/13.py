path = "./13.txt"
col1path = "./col1.txt"
col2path = "./col2.txt"

with open(path,"w", encoding="utf-8") as out_file, \
        open(col1path, "r", encoding="utf-8") as col1_file, \
        open(col2path, "r", encoding="utf-8") as col2_file:
    cols1 = col1_file.readlines()
    cols2 = col2_file.readlines()
    for i in range(len(cols1)):
        out_file.writelines (cols1[i].replace('\n','') + "\t" + cols2[i])


