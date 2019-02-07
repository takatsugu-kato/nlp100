import redis
import gzip
import sys

print ("アーティスト名を入力")
artist = input('>> ')

r = redis.StrictRedis(host='localhost', port=6379, db=0)

results = r.keys(artist + '\t*')
if results:
    for key in results:
        name, id = key.decode().split("\t")
        print (name + "(" + id + "): " + r.get(key).decode())
else:
    print ("None")
