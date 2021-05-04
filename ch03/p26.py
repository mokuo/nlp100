import re

with open("./uk.txt") as f:
    str = f.read()

template_pattern = re.compile("\{\{基礎情報 国\n([\s\S]+)\n\}\}\n")
template_match = template_pattern.search(str)
basic_info = template_match.group(1)
basic_info_list = basic_info.split("\n")

args_pattern = re.compile("\|(\S+)\s+=\s?(.+)")
emphasis_pattern = re.compile("'{2,}([^']+)'{2,}")
dic = {}
for bi in basic_info_list:
    args_match = args_pattern.search(bi)
    if args_match:
        key = args_match.group(1)
        value = args_match.group(2)
        replaced_value = re.sub(emphasis_pattern, "\\1", value)
        dic[key] = replaced_value

print(dic)
