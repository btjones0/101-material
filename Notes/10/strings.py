s = "hello"
s[1] = 'u' # Nope!  Strings are immutable!!!

# But what if I really want a string that like the one I have, but
# with a 'u' at index 1?  We have to turn s into a list of
# characters!

lst = [c for c in s]
lst[1] = 'u'
print(lst) # We're almost there!  But this isn't quite what I want...

print("".join(lst)) # Explain this!

print(", ".join(lst))
