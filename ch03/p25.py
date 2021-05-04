import re

with open("./uk.txt") as f:
    str = f.read()

template_pattern = re.compile("\{\{基礎情報 国\n([\s\S]+)\n\}\}\n")
template_match = template_pattern.search(str)
basic_info = template_match.group(1)
basic_info_list = basic_info.split("\n")

pattern = re.compile("\|(\S+)\s+=\s?(.+)")
dic = {}
for bi in basic_info_list:
    match = pattern.match(bi)
    if match:
        dic[match.group(1)] = match.group(2)

print(dic)
