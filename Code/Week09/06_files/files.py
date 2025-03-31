# We want to be able to run:
#
#   python3 files.py name_of_file
import sys

try:
    my_file = open(sys.argv[1], "r")
except FileNotFoundError:
    print("ERROR: The file %r doesn't exist!" % sys.argv[1])
    sys.exit(1)
except IndexError:
    print("ERROR: No file name provided!")
    sys.exit(1)
except PermissionError:
    print("ERROR: You don't have permission to open %r" % sys.argv[1])
    sys.exit(1)

try:
    line_number = 1
    for line in my_file:
        print("%2d: %s" % (line_number, line.rstrip()))
        line_number += 1
finally:
    my_file.close()
