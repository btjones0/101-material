import sys

# NOTE: Want to be able to type:
#
# python3 files.py <file_to_read>

my_file = open(sys.argv[1], "r")

line_number = 1
for line in my_file:
    print("{:2d}: {:s}".format(line_number, line.rstrip()))
    line_number += 1

my_file.close()
