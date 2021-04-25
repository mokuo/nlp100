str1 = "パトカー"
str2 = "タクシー"

list1 = list(str1)
list2 = list(str2)

result = ""

for i in range(len(list1)):
    result += list1[i]
    result += list2[i]

print(result)
