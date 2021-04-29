input_file = open("./popular-names.txt")
col1_file = open("./col1.txt", mode="w")
col2_file = open("./col2.txt", mode="w")

for line in input_file:
    cols = line.split("\t")
    col1_file.write(f"{cols[0]}\n")
    col2_file.write(f"{cols[1]}\n")

input_file.close()
col1_file.close()
col2_file.close()
