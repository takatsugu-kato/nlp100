string1 = "パトカー"
string2 = "タクシー"
result = ''
zip_iter = zip(string1, string2)
for (a,b) in zip_iter:
    result +=a + b
print (result)
