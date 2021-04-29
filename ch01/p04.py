a = [1, 5, 6, 7, 8, 9, 15, 16, 19]


def main(str: str) -> dict[str, int]:
    words = str.replace(",", "").replace(".", "").split(" ")
    result = dict()

    for i in range(len(words)):
        if (i+1 in a):
            result[words[i][0:1]] = i
        else:
            result[words[i][0:2]] = i

    return result
