# 26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ．

import re


def remove_emphasis(str: str) -> str:
    emphasis_pattern = re.compile("'{2,}([^']+)'{2,}")
    return re.sub(emphasis_pattern, "\\1", str)


def remove_internal_link(str: str) -> str:
    internal_pattern = re.compile("\[\[([^\]\|]+)\|?[^\]]+\]\]")
    sub_str = re.sub(internal_pattern, "\\1", str)
    if sub_str.startswith("ファイル:"):
        return str
    else:
        return sub_str


with open("./uk.txt") as f:
    str = f.read()

template_pattern = re.compile("\{\{基礎情報 国\n([\s\S]+)\n\}\}\n")
template_match = template_pattern.search(str)
basic_info = template_match.group(1)
basic_info_list = basic_info.split("\n")

args_pattern = re.compile("\|(\S+)\s+=\s?(.+)")
dic = {}
for bi in basic_info_list:
    args_match = args_pattern.search(bi)
    if args_match:
        key = args_match.group(1)
        value = args_match.group(2)
        value = remove_emphasis(value)
        value = remove_internal_link(value)
        dic[key] = value

print(dic)
