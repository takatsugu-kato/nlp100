def isStopWord(word):
    if word in stop_words:
        return True
    else:
        return False

stop_words = ["a", "the", "of", "an"]

print (isStopWord("tdhe"))