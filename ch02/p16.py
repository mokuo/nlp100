N = int(input())

with open("./popular-names.txt") as f:
    lines = f.readlines()
    len = len(lines)
    gyou = len // N

    i = 0
    for line in lines:
        i = i + 1
        if i % gyou == 0:
            print()
        print(line.rstrip("\n"))
