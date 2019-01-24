def parse_neko(path):
    sentences = []
    sentence = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.replace('\n','')
            if (line == "EOS"):
                if (sentence):
                    sentences.append(sentence)
                sentence = []
                continue
            else:
                morpheme = {}
                temp = line.split('\t')
                temp_morpheme = temp[1].split(',')
                morpheme = {
                    'surface': temp[0],
                    'base': temp_morpheme[6],
                    'pos': temp_morpheme[0],
                    'pos1': temp_morpheme[1],
                }
                sentence.append(morpheme)
    return sentences

mecab_file = "./neko.txt.mecab"
morpheme_neko = parse_neko(mecab_file)
consecutive_nouns =set()
for sentence in morpheme_neko:
    nouns = ""
    nouns_count = 0
    for morpheme in sentence:
        if(morpheme['pos'] == "名詞"):
            nouns = nouns + morpheme['surface']
            nouns_count = nouns_count + 1
        else:
            if nouns_count > 1:
                consecutive_nouns.add(nouns)
            nouns_count = 0
            nouns = ""
    if nouns_count > 1:##名詞で終わる行があったら入らないので最後にも判定する
        consecutive_nouns.add(nouns)

print(consecutive_nouns)