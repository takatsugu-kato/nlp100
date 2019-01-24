import json
import gzip

with gzip.open('./jawiki-country.json.gz', 'rt', encoding='utf-8') as f:
    for line in f:
        json_data = json.loads(line)
        if (json_data['title']) == "イギリス":
            print (json_data['text'])
            break