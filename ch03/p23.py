import re

with open("./uk.txt") as f:
    for line in f:
        pattern = re.compile("(={2,})([^=]+)={2,}")
        match = pattern.match(line)
        if(match):  # ==国名==
            section = match.group(1)  # ==
            section_name = match.group(2)  # 国名
            print(f"{len(section)-1} {section_name}")
