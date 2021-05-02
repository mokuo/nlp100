import collections

col1 = []

with open("./popular-names.txt") as f:
    for line in f:
        col1.append(line.split("\t")[0])


c = collections.Counter(col1)

with open("./output.txt", mode="w") as of:
    for t in c.most_common():
        of.write(f"{t[1]} {t[0]}\n")

# cut -f 1 popular-names.txt | sort | uniq -c | sort -n -r > sh_
