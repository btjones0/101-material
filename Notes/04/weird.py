def main():
   x = float(input("x: "))
   y = input("y: ")

   z = some_function(x + 3)

   if z < 6.2 and y != "hi":
      y = some_other_function(y)

   if x > 8:
      x -= 5
   if x > 4:
      x = x ** 2
   else:
      x = x / 3

   print("x: {:.1f}, y: {:s}, z: {:.2f}".format(x, y, z))

def some_function(m):
   n = m / 2
   return n

def some_other_function(p):
   if len(p) > 4:
      return "long"
   else:
      return "short"

if __name__ == '__main__':
   main()
