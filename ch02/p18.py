lines = []

with open("./popular-names.txt") as f:
    for line in f:
        lines.append(line.split("\t"))

tmp = sorted(lines, key=lambda cols: int(cols[2]))
result = list(map(lambda cols: "\t".join(cols), tmp))

with open("./output.txt", mode="w") as of:
    of.writelines(result)

# cut -f 3 popular-names.txt | sort -n > sh_output.txt
