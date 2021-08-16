from common import flatten_neko


def sorted_cnt() -> list[(str, int)]:
    neko = flatten_neko()

    # 単語をキーにカウント
    cnt = {}

    for m in neko:
        word: str = m['base']

        if (word in cnt):
            cnt[word] += 1
        else:
            cnt[word] = 1

    return sorted(cnt.items(), key=lambda x: x[1], reverse=True)


# print(sorted_cnt())
