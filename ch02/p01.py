with open("./popular-names.txt") as f:
    lines = f.readlines()
    print(len(lines))  # `wc -l popular-names.txt` で確認
