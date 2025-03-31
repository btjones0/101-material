def do_you_want_to_continue():
   answer = input("Do you want to continue (y/n)? ")

   while answer == 'y':
      answer = input("Do you want to continue (y/n)? ")

   print("Goodbye!")

if __name__ == '__main__':
   do_you_want_to_continue()
