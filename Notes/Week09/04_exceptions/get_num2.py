try:
    num = float(input("Please enter a number: "))
    print("The reciprocal of %.2f is %.2f" % (num, 1 / num))
except ZeroDivisionError:
    print("ERROR: Zere has no real reciprocal!")
except ValueError:
    print("ERROR: That's not a number!")
