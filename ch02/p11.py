import re

results = []

with open("./popular-names.txt") as f:
    for line in f:
        results.append(re.sub("\t", " ", line))

with open("./output.txt", mode="w") as f:
    # sed s/$'\t'/$' '/g popular-names.txt > ./output2.txt
    f.writelines(results)
