# First we import the 'sys' module.  It contains a couple things that
# we'll be using
import sys


# This is the argument vector (old term for list).  It is a list of
# all the arguments passed to your program on the command line.
print(sys.argv)

# NOTE: We notice that index 0 is the name of our program.  This will
# ALWAYS be the case.

# We can also print it's length.
print(len(sys.argv))

# We can loop over all the arguments
for arg in sys.argv:
    print(arg)
