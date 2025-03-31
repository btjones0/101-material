is_valid_input = False

while not is_valid_input:
    try:
        value = int(input("Enter a number: "))
        is_valid_input = True
    except ValueError:
        print("ERROR: That's not an integer!\nPlease try again.")

print("You entered the number %d." % value)
