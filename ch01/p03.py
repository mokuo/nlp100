def main(str: str) -> list[int]:
    words = str.replace(",", "").replace(".", "").split(" ")
    return list(map(word_len, words))


def word_len(str: str) -> int:
    return len(str)
