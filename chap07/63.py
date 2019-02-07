import redis
import gzip
import json

r = redis.StrictRedis(host='localhost', port=6379, db=0)
with gzip.open("./artist.json.gz", "rt", encoding="utf-8") as fi:
    for line in fi:
        d = json.loads(line)
        values = d.get("tags","None")
        if not values == "None":
            for value in values:
                r.rpush(d["name"] + "\t" + str(d["id"]), str(value["count"]) + "\t" + value["value"])
        else:
            r.rpush(d["name"] + "\t" + str(d["id"]), "None")

def join_count_name(text):
    count, name = text.split("\t")
    return name + "[" + str(count) + "]"


print ("アーティスト名を入力")
artist = input('>> ')

results = r.keys(artist + '\t*')
if results:
    for key in results:
        name, id = key.decode().split("\t")
        tags = r.lrange(key,0,-1)
        if tags[0].decode() == "None":
            print (name + "(" + id + "): None")
        else:
            print (name + "(" + id + "): " + ", ".join(map(lambda x: join_count_name(x.decode()),tags)))
else:
    print ("None")
