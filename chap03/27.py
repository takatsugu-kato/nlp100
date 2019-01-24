import json
import gzip
import re

def remove_markup(matchobj):
    link = matchobj.group(1).split('|')
    if (len(link) >= 2):
        return link[1]
    else:
        return link[0]

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
            content = splitted_element[1]
            content = re.sub(r'(\'{2,5})(.*?)\1', r'\2', content)
            content = re.sub(r'\[\[(?!ファイル|File)(.*?)\]\]', remove_markup, content)
            template_dic[splitted_element[0]] = content

with gzip.open('./jawiki-country.json.gz', 'rt', encoding='utf-8') as f:
    for line in f:
        json_data = json.loads(line)
        if (json_data['title']) == "イギリス":
            extract_template (json_data['text'])
            break