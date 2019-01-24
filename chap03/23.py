import json
import gzip
import re

def print_section_name(lines):
    pattern = r'^(==+)\s*([^=]*?)\s*\1$'
    repatter = re.compile(pattern)
    for line in lines:
        result = repatter.search(line)
        if (result):
            print (f'{len(result.group(1))-1} : {result.group(2)}')

with gzip.open('./jawiki-country.json.gz', 'rt', encoding='utf-8') as f:
    for line in f:
        json_data = json.loads(line)
        if (json_data['title']) == "イギリス":
            print_section_name (json_data['text'].split("\n"))
            break