from _30 import neko


def flatten_neko() -> list[dict]:
    neko_result = neko()
    flatten: list[dict] = []

    # morpheme: 形態素
    for m_list in neko_result:
        for m in m_list:
            flatten.append(m)

    return flatten
