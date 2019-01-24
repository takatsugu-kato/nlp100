import json
import gzip
import re

def print_category(lines):
    pattern = r'\[\[Category:'
    repatter = re.compile(pattern)
    for line in lines:
        result = repatter.match(line)
        if (result):
            print (line)


with gzip.open('./jawiki-country.json.gz', 'rt', encoding='utf-8') as f:
    for line in f:
        json_data = json.loads(line)
        if (json_data['title']) == "イギリス":
            print_category (json_data['text'].split("\n"))
            break