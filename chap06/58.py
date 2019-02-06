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

class Dependencies:
    def __init__(self, dep_type, governor_id, dependent_id, text):
        self.type = dep_type
        self.governor_id = governor_id
        self.dependent_id = dependent_id
        self.text = text

def createDependencies(et):
    dependencies = {}
    for dep in et:
        def_type = dep.get("type")
        if not def_type == "punct":
            governor_id = dep.find('governor').attrib.get("idx")
            dependent_id = dep.find('dependent').attrib.get("idx")
            text = dep.find('dependent').text
            dep = Dependencies(def_type ,governor_id, dependent_id, text)
            dependencies[dependent_id] = dep
    return dependencies

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

    sentences = root.iterfind('./document/sentences/sentence')
    for sentence in sentences:
        sentence_id = sentence.get("id")
        dependencies_xml = sentence.find('./dependencies[@type="basic-dependencies"]')
        dependencies = createDependencies(dependencies_xml)
        for dep in dependencies.values():
            found=next((temp for temp in dependencies.values() if dep.type=="nsubj" and temp.type=="dobj" and dep.governor_id == temp.governor_id) ,None)
            if found:
                print (dep.text + "\t" + dependencies[dep.governor_id].text + "\t" + found.text + "\t")