# Let's write a loop that while continue until the user wants it to
# stop.
def do_you_want_to_continue():
    answer = 'y'

    while answer == 'y':
        answer = input('Do you want to continue (y/n)? ')

    print('Goodbye!')


# Let's write a function that takes a number as input.  It then asks the
# user for values until they total more than that number.  Then we'll
# print the total.
def count_until(value):
    total = 0

    while total < value:
        # total = total + int(input('Enter a number: '))
        total += int(input('Enter a number: '))

    print('Total is', total)


count_until(20)
