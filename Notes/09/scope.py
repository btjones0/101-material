def main():
   lst = [1, 2, 3]
   y = func(lst)

   print("Last element of 'lst' is:", lst[-1])
   print("y is:", y)

def func(my_list):
   my_list.append(10)
   return 0

if __name__ == '__main__':
   main()
