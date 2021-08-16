from enum import Flag
from common import flatten_neko

neko = flatten_neko()

# 単語をキーにカウント
cnt = {}

for m in neko:
    word: str = m['base']

    if (word in cnt):
        cnt[word] += 1
    else:
        cnt[word] = 1

sorted_cnt = sorted(cnt.items(), key=lambda x: x[1], reverse=True)

print(sorted_cnt)
