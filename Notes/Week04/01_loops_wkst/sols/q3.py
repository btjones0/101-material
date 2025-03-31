cans = 0
people = 0

while cans < 100:
    cans += int(input("How many cans? "))
    people += 1

print("Total donations: %d" % people)
print("Total number of cans: %d" % cans)
