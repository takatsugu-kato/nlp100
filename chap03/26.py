import json
import gzip
import re

def extract_template(line):
    pattern = r'{{基礎情報(.*)^}}$'
    repatter = re.compile(pattern, flags=(re.MULTILINE | re.DOTALL))
    result = repatter.search(line)
    if (result):
        template_dic = {}
        elements = re.split(r'^\|', result.group(1), flags=re.MULTILINE)
        elements.pop(0)
        for element in elements:
            splitted_element = element.split(' = ')
            template_dic[splitted_element[0]] = re.sub(r'(\'{2,5})(.*?)\1', r'\2', splitted_element[1])

with gzip.open('./jawiki-country.json.gz', 'rt', encoding='utf-8') as f:
    for line in f:
        json_data = json.loads(line)
        if (json_data['title']) == "イギリス":
            extract_template (json_data['text'])
            break