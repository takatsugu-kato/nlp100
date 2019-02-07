import redis
import gzip
import json

r = redis.StrictRedis(host='localhost', port=6379, db=0)
with gzip.open("./artist.json.gz", "rt", encoding="utf-8") as fi:
    for line in fi:
        d = json.loads(line)
        value = d.get("area","None")
        r.set(d["name"] + "\t" + str(d["id"]), value)
print (r.get("George Gao\t56188") )
