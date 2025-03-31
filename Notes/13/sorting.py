# Suppose that I have a list of numbers
nums = [4, 6, -1, 8, 19]

# How might I sort it?  We'll get into more details of exactly "how"
# a little later, for now let's focus on how to get Python to do it
# for us

# sorted(list) will make a new list that contains the same values as
# the old one, but sorted
print(sorted(nums))
# and the original list is left unchanged
print(nums)

# Whereas, list.sort() returns None and sorts the list in place
nums.sort()
print(nums)  # so nums is now sorted

# We can sort in reverse (i.e., decscending order)!
nums.sort(reverse=True)
print(nums)
