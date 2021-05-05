import re
from IPython import embed

result = []

with open("./neco.txt.mecab") as f:
    pattern = re.compile("(?P<surface>.+)\t(?P<info>.+)")
    dics = []
    dic = {}
    for line in f:
        if line == "EOS\n":
            if dics != []:
                result.append(dics)
                dics = []
        else:
            match = pattern.match(line)
            dic["surface"] = match["surface"]

            # 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
            info = match["info"].split(",")
            dic["pos"] = info[0]
            dic["pos1"] = info[1]
            dic["base"] = info[6]

            dics.append(dic)
            dic = {}

print(result)
