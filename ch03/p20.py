import re

with open("./jawiki-country.json") as f:
    for line in f:
        match = re.match(r'{"title": "イギリス", "text": "(.+)"}', line)
        if (match):
            with open("./uk.txt", mode="w") as of:
                of.write(match.group(1))
            break
