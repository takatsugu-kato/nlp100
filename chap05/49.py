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
    def get_chunk_base(self):
        surface = ''
        for morph in self.morphs:
            if(morph.pos == "動詞"):
                surface += morph.base
                return surface
            else:
                surface += morph.base
    def get_last_particle(self):
        for morph in reversed(self.morphs):
            if(morph.pos == "助詞"):
                return morph.surface
        return ""
    def get_surface_masked_noun(self, mask, delete=False):
        surface = ''
        for morph in self.morphs:
            if(morph.pos != "記号"):
                if(morph.pos == "名詞"):
                    surface += mask
                    if delete:
                        return surface
                else:
                    surface += morph.surface
        return surface


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

def print_to_root(chunk_id, chunks):
    print (chunks[chunk_id].get_chunk_surface(), end="")
    out_file.writelines(chunks[chunk_id].get_chunk_surface())
    if (chunks[chunk_id].dst > 0):
        print (" -> ", end="")
        out_file.writelines (" -> ")
        print_to_root (chunks[chunk_id].dst, chunks)
    else:
        out_file.writelines ("\n")
        print ("\n")

cabocha_file = "./test.cabocha"
morpheme_neko = parse_neko(cabocha_file)

with open('./49.txt', 'w', encoding='utf-8') as out_file:
    for sentence in morpheme_neko:
        indexs_noun = []
        for i in range(len(sentence)):
            if (sentence[i].is_contain_noun):
                indexs_noun.append(i)

        for i, index_x in enumerate(indexs_noun[:-1]):
            for index_y in indexs_noun[i + 1:]:
                root_x = set()
                meet_y = False
                index_dup  = -1
                dst = sentence[index_x].dst
                while dst != -1:
                    if dst == index_y:
                        meet_y = True
                        break
                    root_x.add(dst)
                    dst = sentence[dst].dst
                if meet_y == False:
                    dst = sentence[index_y].dst
                    while dst != -1:
                        if dst in root_x:
                            index_dup  = dst
                            break
                        dst = sentence[dst].dst

                if index_dup == -1:
                    out_file.write(sentence[index_x].get_surface_masked_noun('X'))
                    dst = sentence[index_x].dst
                    while dst != -1:
                        if dst == index_y:
                            out_file.write(
                                    ' -> ' + sentence[dst].get_surface_masked_noun('Y',True))
                            break
                        else:
                            out_file.write(
                                    ' -> ' + sentence[dst].get_chunk_surface())
                        dst = sentence[dst].dst
                    out_file.write('\n')
                else:
                    out_file.write(sentence[index_x].get_surface_masked_noun('X'))
                    dst = sentence[index_x].dst
                    while dst != index_dup:
                        out_file.write(' -> ' + sentence[dst].get_chunk_surface())
                        dst = sentence[dst].dst
                    out_file.write(' | ')

                    # Yからぶつかる手前までを出力
                    out_file.write(sentence[index_y].get_surface_masked_noun('Y'))
                    dst = sentence[index_y].dst
                    while dst != index_dup:
                        out_file.write(' -> ' + sentence[dst].get_chunk_surface())
                        dst = sentence[dst].dst
                    out_file.write(' | ')

                    # ぶつかったchunkを出力
                    out_file.write(sentence[index_dup].get_chunk_surface())
                    out_file.write('\n')




