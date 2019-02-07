import redis
import gzip
import sys

area = "Japan"

r = redis.StrictRedis(host='localhost', port=6379, db=0)

# results = r.keys('*')
# count = 0
# for key in results:
#     if r.get(key).decode() == area:
#         count = count +1
# print (count)

cur = 0
count = 0
while True:
    cur, keys = r.scan(cur, match="*", count=10000)
    for key in keys:
        if r.get(key).decode() == area:
            count = count + 1
    if cur == 0:
        break
print (count)