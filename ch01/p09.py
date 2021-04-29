import random
from IPython import embed


def main(str: str):
    words = str.split(" ")
    a = map(sort_word, words)
    return list(a)


def sort_word(str: str):
    if len(str) <= 4:
        return str
    else:
        first = str[0]
        last = str[len(str)-1]
        other = str[1:len(str)-1]
        others = list(other)
        random.shuffle(others)
        return first + "".join(others) + last
