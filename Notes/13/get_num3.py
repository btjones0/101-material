is_valid_input = False

while not is_valid_input:
   try:
      value = int(input("Enter an integer: "))
      is_valid_input = True
   except ValueError:
      print("ERROR: Please enter an integer.\n")

print("You entered: {:d}.".format(value))
