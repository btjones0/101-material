last = 12
sum_of_squares = 0

for number in range(last + 1):
    sum_of_squares += number ** 2
    print("The number %2d squared is %3d." % (number, number ** 2))

print("The sum of the squares is %d." % sum_of_squares)
