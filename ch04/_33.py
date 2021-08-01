from _30 import neko

neko_result = neko()
result: list[str] = []

# 形態素のリストから、「の」で連結されている名詞句を返す


def __np(m_list: list[dict]) -> str:
    r = None

    # 「の」の位置を返す
    no_indexes = [i for i, m in enumerate(m_list) if m['surface'] == 'の']

    for no_index in no_indexes:
        both_np = __both_np(m_list, no_index)
        if both_np:
            r = m_list[no_index-1]['surface'] + \
                m_list[no_index]['surface'] + m_list[no_index+1]['surface']

    return r

# 前後が名詞かどうか


def __both_np(m_list: list[dict], index: int) -> bool:
    if (index-1) < 0:
        return False

    if (index+1) >= len(m_list):
        return False

    before_pos = m_list[index-1]['pos']
    after_pos = m_list[index+1]['pos']

    return before_pos == '名詞' and after_pos == '名詞'


# morpheme: 形態素
for m_list in neko_result:
    np_result = __np(m_list)

    if np_result is not None:
        result.append(np_result)

print(len(result))
