char = 'a' # How is this stored in a computer?

# It's stored as a number!!!  (Bring up ASCII table.)
# Strings are just numbers!  How might I get that number?

print(ord(char)) # 97
print(chr(98))   # 'b'

# For the most part, we don't really care which character is which
# number.  One thing that we do care about is where 'A' and 'a' are
# relative to each other.  'A' is 32 before 'a'.

print(char.islower()) # True
print(char.isupper()) # False
