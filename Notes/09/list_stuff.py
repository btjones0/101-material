my_list = [2, 3, 7.1, "hi"]
my_list
my_list[0]
my_list[3]
my_list[4]
my_list[100] # Guesses???
my_list[-2]  # Guesses???

# Lists are mutable!!
my_list[2] = -45.1
my_list
my_list.append(9) # we can add more stuff to the end!

list2 = [8, 0]
my_list + list2
my_list
list2
my_list = my_list + list2
my_list
my_list * 2
my_list
my_list *= 2

# Listception!
my_list[2] = ["dog", -8]
my_list
my_list[2]
my_list[2][0]

# Empty Lists!
p = []
p
p.append(4)
p

# We can compare lists!
l = [1, 2, 3, 4]
m = [1, 2, 3, 4]
l == m
n = [3, 2, 1, 4]
m == n
