doc1 = "Python is a powerful programming language"
doc2 = "Python is used for programming and data analysis"
doc3 = "I love eating biryani in Hyderabad"


def tokenize(text):
    l = text.split()
    for e in l:
        e = e.replace(".,;","")
    return l

print(tokenize(doc1))