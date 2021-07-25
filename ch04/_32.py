from _30 import neko

neko_result = neko()
flatten: list[dict] = []

# morpheme: 形態素
for m_list in neko_result:
    for m in m_list:
        flatten.append(m)

result = [m["base"] for m in flatten]
print(result)
