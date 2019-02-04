from pycorenlp import StanfordCoreNLP
import xml.etree.ElementTree as ET

path = "./nlp.txt"
nlp = StanfordCoreNLP('http://localhost:9000')

def parseLines (path):
    with open(path,"r",encoding="utf-8") as f:
        data = f.readlines()
    lines = data
    return lines

def getAnnotateXML (text):
    output = nlp.annotate(text, properties={
        'annotators': 'lemma',
        'outputFormat': 'xml'
    })
    return output

lines = parseLines(path)
xml = getAnnotateXML(lines[1])


root = ET.fromstring(xml)
for sentences in root[0]:
    for sentence in sentences:
        for tokens in sentence:
            for token in tokens:
                print (token.find('word').text)