import re


def parse_lines (path):
    with open(path,"r",encoding="utf-8") as f:
        data = f.readlines()
    lines = []
    separater = [r"\.",";",":",r"\?","!"]
    pattern = "(" + "|".join(separater)  + ") ([A-Z])"
    for line in data:
        line = line.strip()
        if (len(line)):
            result = re.sub(pattern, "\\1\n\\2", line)
            lines.extend(result.split("\n"))
    return lines

path = "./nlp.txt"
lines = parse_lines(path)

for line in lines:
    print ("\n".join(line.split(" ")) + "\n")