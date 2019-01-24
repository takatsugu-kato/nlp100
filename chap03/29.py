import json
import gzip
import re
import requests

def remove_internal_link_markup(matchobj):
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
            content = re.sub(r'(\'{2,5})(.*?)\1', r'\2', content)#強調文字マークアップの削除
            content = re.sub(r'\[\[(?!ファイル|File)(.*?)\]\]', remove_internal_link_markup, content)#内部リンクマークアップの削除
            content = re.sub(r'\[\[(File|ファイル):(.*?)\|.*?\]\]', r'\2', content)#ファイルリンクマークアップの削除
            content = re.sub(r'\{\{lang\|.*?\|(.*?)\}\}', r'\1', content, flags=(re.MULTILINE | re.DOTALL))#テンプレートマークアップの削除
            content = re.sub(r'\[https?://.*? (.*?)\]', r'\1', content, flags=(re.MULTILINE | re.DOTALL))#外部リンクの削除
            template_dic[splitted_element[0]] = content
        for key in template_dic:
            print ((f"{key}: {template_dic[key]}"))
        #国旗画像
        flag_filename = template_dic['国旗画像']
        S = requests.Session()
        URL = "https://www.mediawiki.org/w/api.php"
        PARAMS = {
            "action":"query",
            "format":"json",
            "prop": "imageinfo",
            "titles":"File:"+flag_filename,
            "iiprop":"url"
        }
        R = S.get(url=URL, params=PARAMS)
        DATA = R.json()
        print(DATA['query']['pages']['-1']['imageinfo'][0]['url'])

with gzip.open('./jawiki-country.json.gz', 'rt', encoding='utf-8') as f:
    for line in f:
        json_data = json.loads(line)
        if (json_data['title']) == "イギリス":
            extract_template (json_data['text'])
            break