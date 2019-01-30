import re

class Morph:
    def __init__(self, s, b, p, p1):
        self.surface = s
        self.base = b
        self.pos = p
        self.pos1 = p1
    def __str__(self):
        return 'surface[{}]\tbase[{}]\tpos[{}]\tpos1[{}]'\
            .format(self.surface, self.base, self.pos, self.pos1)

class Chunk:
    def __init__(self):
        self.morphs = []
        self.dst = int()
        self.srcs = []
        self.is_contain_verb = False
        self.is_contain_noun = False
        self.is_contain_particle = False
    def __str__(self):
        surface = ''
        for morph in self.morphs:
            surface += morph.surface
        return '{}\tdst[{}]\tsrcs{}'\
            .format(surface, self.dst, self.srcs)
    def get_chunk_surface(self):
        surface = ''
        for morph in self.morphs:
            if(morph.pos != "記号"):
                surface += morph.surface
        return surface
    def get_last_particle(self):
        for morph in reversed(self.morphs):
            if(morph.pos == "助詞"):
                return morph.surface


def parse_neko(path):
    sentences = []
    chunks = dict()
    chunk_id = -1
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.replace('\n','')
            if (line[0] == "*"):
                temp = line.split(' ')
                chunk_id = int(temp[1])
                dst = int(re.search(r'(.*?)D', temp[2]).group(1))
                if chunk_id not in chunks.keys():
                    chunks[chunk_id] = Chunk()
                chunks[chunk_id].dst = dst
                if (dst > 0):
                    if dst not in chunks.keys():
                        chunks[dst] = Chunk()
                    chunks[dst].srcs.append(chunk_id)
                continue
            if (line == "EOS"):
                if (chunks):
                    sorted_chunks = sorted(chunks.items(), key=lambda x: x[0])
                    sentences.append(list(zip(*sorted_chunks))[1])#それぞれのchunkのkey0に値０がはいるので
                chunks = dict()
                continue
            else:
                morpheme = {}
                temp = line.split('\t')
                temp_morpheme = temp[1].split(',')
                morpheme = Morph(temp[0], temp_morpheme[6], temp_morpheme[0], temp_morpheme[1])
                chunks[chunk_id].morphs.append(morpheme)
                if temp_morpheme[0] == "動詞":
                    chunks[chunk_id].is_contain_verb = True
                if temp_morpheme[0] == "名詞":
                    chunks[chunk_id].is_contain_noun = True
                if temp_morpheme[0] == "助詞":
                    chunks[chunk_id].is_contain_particle= True
    return sentences

cabocha_file = "./test.cabocha"
morpheme_neko = parse_neko(cabocha_file)

with open('./45.txt', 'w', encoding='utf-8') as out_file:
    for i, sentence in enumerate(morpheme_neko):
        for j in range(len(sentence)):
            if (sentence[j].morphs[0].pos == "動詞"):
                kakus = []
                for src_id in sentence[j].srcs:
                    if (sentence[src_id].is_contain_particle):
                        kakus.append(sentence[src_id].get_last_particle())
                if (kakus):
                    out_file.writelines(sentence[j].morphs[0].base + "\t" + " ".join(sorted(kakus)) + "\n")
                    print (sentence[j].morphs[0].base + "\t" + " ".join(kakus))


