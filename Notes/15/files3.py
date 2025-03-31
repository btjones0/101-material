import sys

# NOTE: Want to be able to type:
#
# python3 files.py <file_to_read>

try:
    my_file = open(sys.argv[1], "r")
except IndexError:
    print("Usage: python3 files.py <file_to_read>")
    sys.exit(1)
except FileNotFoundError:
    print("No such file or directory: '{}'".format(sys.argv[1]))
    sys.exit(1)
except PermissionError:
    print("Permission denied: '{}'".format(sys.argv[1]))
    sys.exit(1)
except:
    print("Some other exception happened")
    sys.exit(1)

line_number = 1
for line in my_file:
    print("{:2d}: {:s}".format(line_number, line.rstrip()))
    line_number += 1
my_file.close()
