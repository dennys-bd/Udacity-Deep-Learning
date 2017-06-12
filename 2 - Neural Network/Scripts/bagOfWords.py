from collections import Counter()

def bag_of_words(text):
    dic = {}
    for word in text.split(' '):
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
    return dic

def bag_of_words2(text):
    return Counter(text.split())