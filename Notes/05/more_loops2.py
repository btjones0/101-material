def count_until(num):
   total = 0
   while num > total:
      total += float(input("Enter a number: "))

   print("Total was", total)

if __name__ == '__main__':
   count_until(20)
