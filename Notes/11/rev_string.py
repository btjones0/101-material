def rev_string(string):
   backwards = []
   for index in range(len(string) - 1, -1, -1):
      backwards.append(string[index])

   return "".join(backwards)

def rev_string(string):
   backwards = list(string)
   i = 0
   j = len(string) - 1
   while i < j:
      temp = rev[i]
      rev[i] = rev[j]
      rev[j] = temp
      i += 1
      j -= 1

   return "".join(backwards)
