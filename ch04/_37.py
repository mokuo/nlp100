from matplotlib import pyplot as plt
from _30 import neko

neko_result = neko()

# 単語をキーにカウント
cnt = {}
words: list[str] = []  # 横軸
values: list[int] = []  # 縦軸


def is_neko(s: list[str]) -> bool:
    for m in s:
        if m['surface'] == '猫':
            return True

    return False


def count_up(word: str):
    if (word in cnt):
        cnt[word] += 1
    else:
        cnt[word] = 1


for s in neko_result:
    if (is_neko(s)):
        for m in s:
            if m['pos'] == '名詞' and m['surface'] != '猫':
                count_up(m['surface'])

sorted_cnt = sorted(cnt.items(), key=lambda x: x[1], reverse=True)

for i in range(10):
    word, value = sorted_cnt[i]
    words.append(word)
    values.append(value)

plt.bar(words, values)
plt.show()
