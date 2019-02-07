import gzip
import pymongo
from pymongo import MongoClient
import datetime
import json
from bson import ObjectId
import time

start = time.time()

client = MongoClient('localhost', 27017)

def support_ObjectId(obj):
    if isinstance(obj, ObjectId):
        return str(obj)     # 文字列として扱う
    raise TypeError(repr(obj) + " is not JSON serializable")

db = client['nlp100']
collection = db['artist']

results = collection.find({"tags.value" : "dance"}).sort("rating.count",pymongo.DESCENDING).limit(10)
for result in results:
    print (result['name'] + "(id:" + str(result["id"]) + "): " + str(result["rating"]["count"]))
    # print(json.dumps(result, ensure_ascii=False, indent=4, sort_keys=True, default=support_ObjectId))

elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")