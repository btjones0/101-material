my_file = open('text_file.txt', 'r')
new_file = open('new_file.txt', 'w')

line_num = 1
for line_of_text in my_file:
    new_file.write("(%d): (%s)\n" % (line_num, line_of_text.rstrip()))
    line_num += 1

my_file.close()
new_file.close()
