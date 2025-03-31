def main():
   secret = 7

   guess = int(input("Enter a number: "))

   if guess == secret:
      print("Congrats!  You were right!")
   else:
      print("You lose!")

if __name__ == '__main__': # We then need to call the main function
   main()
