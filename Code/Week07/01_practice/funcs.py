# 1. list_pow
def list_pow(numbers, exponent):
    return [number ** exponent for number in numbers]


# 2. all_passing
def all_passing(all_grades, threshold=70):
    result = []

    for student in all_grades:
        result.append(student_pass(student, threshold))

    return result


def student_pass(student_grades, threshold):
    for exam_grade in student_grades:
        if exam_grade < threshold:
            return False
    return True


# 3. max_sequence_length
def max_sequence_length(numbers):
    max_length = 0
    prev_number = None
    prev_length = 0

    for number in numbers:
        if number == prev_number:
            prev_length += 1
        else:
            prev_length = 1
            prev_number = number

        if prev_length > max_length:
            max_length = prev_length

    return max_length


# 4. alpha_only
def alpha_only(list_of_strings):
    result = []

    for string in list_of_strings:
        # if string.isalpha():
        if is_only_alpha(string):
            result.append(string)

    return result


def is_only_alpha(string):
    for char in string:
        if not is_char_alpha(char):
            return False

    return True


def is_char_alpha(char):
    val = ord(char)

    return (
        ord('a') <= val and val <= ord('z') or
        ord('A') <= val and val <= ord('Z')
    )


# 5. avoids
