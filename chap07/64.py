import gzip
import pymongo
from pymongo import MongoClient
import datetime
import json

client = MongoClient('localhost', 27017)

db = client['nlp100']
collection = db['artist']

with gzip.open("./artist.json.gz","rt",encoding="utf-8") as fi:
    for line in fi:
        json_line = json.loads(line)
        result = collection.insert_one(json_line)
collection.create_index([('name', pymongo.ASCENDING)])
collection.create_index([('aliases.name', pymongo.ASCENDING)])  
collection.create_index([('tags.value', pymongo.ASCENDING)])
collection.create_index([('rating.value', pymongo.ASCENDING)])