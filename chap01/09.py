import random

def Typoglycemia(string):
    words = string.split(' ')
    result = []
    for word in words:
        if (len(word) > 4):
            to_shuffle_chara = list(word[1:-1])
            random.shuffle(to_shuffle_chara)
            result.append(word[0] + ''.join(to_shuffle_chara) + word[-1])
        else:
            result.append(word)
    return ' '.join(result)

string = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind . "

result = Typoglycemia(string)
print (result)


