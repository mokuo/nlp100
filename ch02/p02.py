import re

results = []

with open("./popular-names.txt") as f:
    for line in f:
        results.append(re.sub("\t", " ", line))

with open("./output.txt", mode="w") as f:
    f.writelines(results)
