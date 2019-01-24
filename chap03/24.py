import json
import gzip
import re

def extract_media_file(lines):
    pattern = r'(File|ファイル):(.*?)\|'
    repatter = re.compile(pattern)
    for line in lines:
        result = repatter.search(line)
        if (result):
            print (result.group(2))

with gzip.open('./jawiki-country.json.gz', 'rt', encoding='utf-8') as f:
    for line in f:
        json_data = json.loads(line)
        if (json_data['title']) == "イギリス":
            extract_media_file (json_data['text'].split("\n"))
            break