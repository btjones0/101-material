lst = [3, -6, 10, 12, 1, 88]

lst[2:4] # can get a sublist!
lst[:4]  # can leave off start (will default to 'beginning')
lst[3:]  # can leave off stop  (will defailt to 'end')
lst[:]

lst[-2:] # we can still use negative indices

lst[3:20] # what will this do??
lst[-20:] # this one?
lst[4:2]  # ?

string = "banana"
string[2:5] # you can slice a string!!

words = ["banana", "hi", "cat", "student", "thing"]
words[1:3]   # a list of strings!!
words[3][:3] # what'll it do???
