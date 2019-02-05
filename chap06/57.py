from pycorenlp import StanfordCoreNLP
import xml.etree.ElementTree as ET
from graphviz import Digraph

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

annotate = getAnnotate(lines[5])
root = ET.fromstring(annotate)

G = Digraph(format="png")
G.attr("node", shape="square", style="filled")

sentences = root.iterfind('./document/sentences/sentence')
for sentence in sentences:
    sentence_id = sentence.get("id")
    dependencies = sentence.find('./dependencies[@type="basic-dependencies"]')
    G.node('literal_'+sentence_id+'_0', label="ROOT")
    for dep in dependencies:
        if not dep.get("type") == "punct":
            governor_id = dep.find('governor').attrib.get("idx")
            dependent_id = dep.find('dependent').attrib.get("idx")
            G.node('literal_'+sentence_id+'_'+dependent_id, label=dep.find('dependent').text)
            G.edge('literal_'+sentence_id+'_'+governor_id, 'literal_'+sentence_id+'_'+dependent_id)
G.render("graphs")