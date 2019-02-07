import gzip
import pymongo
from pymongo import MongoClient
import datetime
import json
from bson import ObjectId

client = MongoClient('localhost', 27017)

def support_ObjectId(obj):
    if isinstance(obj, ObjectId):
        return str(obj)     # 文字列として扱う
    raise TypeError(repr(obj) + " is not JSON serializable")

db = client['nlp100']
collection = db['artist']

print (collection.count_documents({"area" : "Japan"}))
