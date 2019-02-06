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
        'annotators': 'parse',
        'outputFormat': 'xml'
    })
    return output

lines = parseLines(path)
xml = getAnnotateXML(lines[1])
with open("./sample.xml","w") as f:
    f.writelines(xml)
# root = ET.fromstring(xml)
# tokens = root.iterfind('./document/sentences/sentence/tokens/token[NER="PERSON"]')
# for token in tokens:
#     print (token.find('word').text)
