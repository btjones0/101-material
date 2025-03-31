last = 10

x = 0
square_sum = 0

while x <= last:
    x_squared = x * x
    print("The number %2d squared is %3d." % (x, x_squared))
    square_sum += x_squared
    x += 1

print("The sum of the squares is %d." % square_sum)
