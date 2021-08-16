import matplotlib.pyplot as plt

from _35 import sorted_cnt

cnt: list[(str, int)] = sorted_cnt()

words: list[str] = []  # 横軸
values: list[int] = []  # 縦軸

for i in range(10):
    word, value = cnt[i]
    words.append(word)
    values.append(value)

print(words)
print(values)

plt.bar(words, values)
plt.show()
