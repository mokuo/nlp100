def main():
    str1 = "パトカー"
    str2 = "タクシー"
    result = ""

    for i in range(len(str1)):
        result += str1[i]
        result += str2[i]

    return result
