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
    def __init__(self, sentence, start, end, head, text, representative):
        self.sentence = sentence
        self.start = start
        self.end = end
        self.head = head
        self.text = text
        self.representative = representative
    def __str__(self):
        return 'sentence[{}]\tstart[{}]\tend[{}]\thead[{}]\ttext[{}]'\
            .format(self.sentence, self.start, self.end, self.head, self.text)

def createCoreferences(et):
    coreferences = []
    coreferences_xml = et.iterfind('./document/coreference/coreference')
    for mentions_xml in coreferences_xml:
        representative = mentions_xml.findtext('./mention[@representative="true"]/text')
        for mention_xml in mentions_xml:
            if not mention_xml.attrib.get("representative") == "true":
                sentence = mention_xml.find("sentence").text
                start = mention_xml.find("start").text
                end = mention_xml.find("end").text
                head = mention_xml.find("head").text
                text = mention_xml.find("text").text
                mention = Mention(sentence,start,end,head,text,representative)
                coreferences.append(mention)
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
            found=next((mention for mention in coreferences if mention.sentence==sentence_id and mention.start==token_id) ,None)
            if found:
                to_print_mention_word = to_print_word
                for num in range(int(found.end) - int(found.start) - 1):
                    to_print_mention_word = to_print_mention_word + " " + tokens[i+1].find("word").text
                    i = i + 1
                to_print_word = found.representative + " (" + to_print_mention_word + ")"
            i = i + 1
            print (to_print_word)