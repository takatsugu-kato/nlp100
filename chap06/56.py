from pycorenlp import StanfordCoreNLP
import xml.etree.ElementTree as ET

path = "./nlp.txt"
nlp = StanfordCoreNLP('http://localhost:9000')

def parseLines (path):
    with open(path,"r",encoding="utf-8") as f:
        data = f.readlines()
    lines = data
    return lines

def getAnnotate (text):
    output = nlp.annotate(text, properties={
        'annotators': 'dcoref',
        'outputFormat': 'xml'
    })
    return output

class Mention:
    def __init__(self, sentence, start, end, head, text):
        self.sentence = sentence
        self.start = start
        self.end = end
        self.head = head
        self.text = text
    def __str__(self):
        return 'sentence[{}]\tstart[{}]\tend[{}]\thead[{}]\ttext[{}]'\
            .format(self.sentence, self.start, self.end, self.head, self.text)

class Coreference:
    def __init__(self):
        self.representative = ""
        self.mentions = []
    def __str__(self):
        surface = ''
        for mention in self.mentions:
            surface += mention.text
        return surface

def createCoreferences(et):
    coreferences_xml = et.iterfind('./document/coreference/coreference')
    coreferences = []
    for mentions_xml in coreferences_xml:
        coreference = Coreference()
        for mention_xml in mentions_xml:
            # if mention.attrib(representative)
            sentence = mention_xml.find("sentence").text
            start = mention_xml.find("start").text
            end = mention_xml.find("end").text
            head = mention_xml.find("head").text
            text = mention_xml.find("text").text
            mention = Mention(sentence,start,end,head,text)
            if mention_xml.attrib.get("representative") == "true":
                coreference.representative = mention
            else:
                coreference.mentions.append(mention)
        coreferences.append(coreference)
    return coreferences

lines = parseLines(path)

for line in lines:
    annotate = getAnnotate(line)
    root = ET.fromstring(annotate)

    coreferences = createCoreferences(root)
    sentences = root.iterfind('./document/sentences/sentence')
    for sentence in sentences:
        sentence_id = sentence.get("id")
        tokens = sentence.find('tokens')
        i = 0
        while i < len(tokens):
            token_id = tokens[i].get("id")

            to_print_word = tokens[i].find('word').text
            ##coreferencesに該当するか確認
            for coreference in coreferences:
                for mention in coreference.mentions:
                    to_print_mention_word = to_print_word
                    if mention.sentence == sentence_id and mention.start == token_id:
                        for num in range(int(mention.end) - int(mention.start) - 1):
                            to_print_mention_word = to_print_mention_word + " " + tokens[i+1].find("word").text
                            i = i + 1
                        to_print_word = coreference.representative.text + " (" + to_print_mention_word + ")"
                        break
            i = i + 1
            print (to_print_word)