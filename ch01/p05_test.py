from p05 import main


def test_main():
    str = "I am an NLPer"

    chars = list(str)
    chars_bi_gram = main(chars, 2)
    assert chars_bi_gram == ["I ", " a", "am", "m ",
                             " a", "an", "n ", " N", "NL", "LP", "Pe", "er"]

    words = str.split(" ")
    words_bi_gram = main(words, 2)
    assert words_bi_gram == ["Iam", "aman", "anNLPer"]
