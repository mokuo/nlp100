def main(strs: list[str], n: int) -> list[str]:
    result = []

    for i in range(len(strs)):
        if i == len(strs) - 1:
            break

        str = ""
        for j in range(n):
            str += strs[i+j]

        result.append(str)

    return result
