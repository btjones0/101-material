my_dictionary = {
    'name': 'Brian',
    'age': 19,
    'gpa': 4.0,
    'classes': [
        {
            'name': 'Fundamentals of Computer Science',
            'grade': 100.0,
            'letter_grade': 'A'
        },
        {
            'name': 'Macroeconomics',
            'grade': 82.3,
            'letter_grade': 'B-'
        },
        {
            'name': 'Linear Algebra III',
            'grade': 95.3,
            'letter_grade': 'A'
        },
        {
            'name': 'Public Speaking',
            'grade': 87.7,
            'letter_grade': 'B+'
        }
    ]
}

# print("%s's first class is %s." % (
#     my_dictionary['name'],
#     my_dictionary['classes'][0]['name']))

for course in my_dictionary['classes']:
    print("%s's grade in %s is %.1f." % (
        my_dictionary['name'],
        course['name'],
        course['grade']))
