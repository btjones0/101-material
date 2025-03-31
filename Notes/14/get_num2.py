try:
   value = int(input("Enter an integer: "))

   # We only get here if there was not an error.
   print("You entered: {:d}.".format(value))
except ValueError:
   print("ERROR: That wasn't an integer.\n")
