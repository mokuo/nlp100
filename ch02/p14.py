N = int(input())

with open("./popular-names.txt") as f:
    i = 0
    for line in f:
        i = i + 1
        if i > N:
            break

        print(line.rstrip("\n"))
