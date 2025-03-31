def main():
    guess = int(input('Enter a number: '))

    secret = 7

    if guess == secret:
        print("Congrats!  You were right!")
    elif guess > secret:
        print("You were too high!")
    elif guess == -12:
        print("You guessed -12, which is wrong.")
    else:
        print("You were too low!")


if __name__ == '__main__':
    main()
