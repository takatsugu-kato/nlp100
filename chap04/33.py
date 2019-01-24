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
verbs_surface =set()
verbs_base =set()
sahen_noun =set()
for sentence in morpheme_neko:
    for morpheme in sentence:
        if (morpheme['pos'] == "動詞"):
            verbs_surface.add(morpheme['surface'])
            verbs_base.add(morpheme['base'])
        if (morpheme['pos1'] == "サ変接続"):
            sahen_noun.add(morpheme['surface'])
print(sahen_noun)