import re
with open("./nlp.txt","r",encoding="utf-8") as f:
    data = f.readlines()

separater = [r"\.",";",":",r"\?","!"]
pattern = "(" + "|".join(separater)  + ") ([A-Z])"

for line in data:
    line = line.strip()
    if (len(line)):
        result = re.sub(pattern, "\\1\n\\2", line)
        print ("\n".join(result.split(" ")) + "\n")