def main():
   secret = 7

   guess = int(input("Enter a number: "))

   if guess == secret:
      print("Congrats!  You were right!")
   else:
      if guess > secret:
         print("You were too high!")
      else:
         print("You were too low!")

if __name__ == '__main__':
   main()
