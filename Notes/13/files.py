# must exist or causes error
in_file = open("text_file.txt", 'r')

# created if doesn't exist, contents erased if it does
out_file = open("new_file.txt", 'w')

line_num = 1
for line in in_file:
   print(line_num, line.rstrip())
   out_file.write("{:d}) {:s}".format(line_num, line))
   line_num += 1

in_file.close()
out_file.close()
