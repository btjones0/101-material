my_dictionary = {
    'name': 'Brian',
    'age': 19,
    'gpa': 4.0,
    'classes': [
        'Fundamentals of Computer Science',
        'Macroeconomics',
        'Linear Algebra III',
        'Public Speaking'
    ]
}

# print("%s's first class is %s." % (
#     my_dictionary['name'],
#     my_dictionary['classes'][0]))

for course in my_dictionary['classes']:
    print(course)
