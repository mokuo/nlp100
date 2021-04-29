import re


def cipher(str: str) -> str:
    a = list(str)
    return "".join(list(map(convert, a)))


def convert(str: str) -> str:
    match = re.search("[a-z]", str)

    if match:
        return chr(219 - ord(str))
    else:
        return str
