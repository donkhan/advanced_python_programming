def factorial(n):
    if n != 0:
        return n * factorial(n-1)
    return 1


def sum_elements(l):
    if len(l) == 0:
        return 0
    return l[0] + sum_elements(l[1:])


def word_count():
    d = {}
    with open("../words.txt", "r", encoding="utf-8") as file:
        content = file.read()
        lines = content.split("\n")
        for line in lines:
            tokens = line.split()
            for token in tokens:
                if token in d:
                    d[token] = d[token] + 1
                else:
                    d[token] = 1
    for key in d.keys():
        print(key + " = " + str(d[key]))


if __name__ == '__main__':
    print(sum_elements([1, 2, 3]))
    print(factorial(4))
    word_count()
