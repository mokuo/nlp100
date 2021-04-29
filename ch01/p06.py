def main(x_str: str, y_str: str):
    x = bi_gram(x_str)
    y = bi_gram(y_str)

    wa = set(x) | set(y)
    seki = set(x) & set(y)
    sa = set(x) - set(y)

    x_se = "se" in x
    y_se = "se" in y

    return [wa, seki, sa, x_se, y_se]


def bi_gram(str: str) -> list[str]:
    result = []

    for i in range(len(str)-1):
        result.append(str[i:i+2])

    return result
