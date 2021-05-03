import re

with open("./uk.txt") as f:
    for line in f:
        pattern = re.compile("\[\[Category:([^\|\]]+)\|?.*\]\]")
        match = pattern.match(line)
        if(match):
            print(match.group(1))
