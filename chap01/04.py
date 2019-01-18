string = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words = string.split(' ')
to_get_first_chara_list = [1, 5, 6, 7, 8, 9, 15, 16, 19]
element_symbols = {}

for i, word in enumerate(words, 1):
    if i in to_get_first_chara_list:
        to_get_count = 1
    else:
        to_get_count = 2
    element_symbols[word[0:to_get_count]] = i

print (element_symbols)