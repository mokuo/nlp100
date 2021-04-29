from IPython import embed

col1_file = open("./col1.txt")
col2_file = open("./col2.txt")
output_file = open("./output.txt", mode="w")

col1_lines = col1_file.readlines()
col2_lines = col2_file.readlines()

for i in range(len(col1_lines)):
    line1 = col1_lines[i].replace("\n", "\t")
    line2 = col2_lines[i]
    output_file.write(line1 + line2)

col1_file.close()
col2_file.close()
output_file.close()
# paste col1.txt col2.txt > sh_output.txt
