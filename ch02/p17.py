strs = []

with open("./popular-names.txt") as f:
    for line in f:
        cols = line.split("\t")
        strs.append(cols[0])

result = sorted(set(strs))
print(len(result))
# print(result)

# python p17.py
# => 136

# cut -f 1 popular-names.txt | sort | uniq | wc -l
# => 136
