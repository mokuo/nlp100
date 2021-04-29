N = int(input())

with open("./popular-names.txt") as f:
    lines = f.readlines()
    len = len(lines)
    for line in lines[len-N:len]:
        print(line.rstrip("\n"))
