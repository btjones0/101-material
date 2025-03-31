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
    for grade in student_grades:
        if grade < threshold:
            return False

    return True


# 3. max_sequence_length
def max_sequence_length(numbers):
    max_length = 0
    current_length = 0
    current_value = None

    for number in numbers:
        if number == current_value:
            current_length += 1
        else:
            current_value = number
            current_length = 1

        if current_length > max_length:
            max_length = current_length

    return max_length


# 4. alpha_only
# NOTE: you didn't need to decompose this as much as I did
def alpha_only(words):
    return [word for word in words if is_only_alpha(word)]


def is_only_alpha(word):
    for letter in word:
        if not (is_lowercase_letter(letter) or is_uppercase_letter(letter)):
            return False

    return True


def is_lowercase_letter(letter):
    return ord('a') <= ord(letter) and ord(letter) <= ord('z')


def is_uppercase_letter(letter):
    return ord('A') <= ord(letter) and ord(letter) <= ord('Z')


# 5. avoids
def avoids(word, forbidden):
    for letter in word:
        for forbidden_letter in forbidden:
            if letter == forbidden_letter:
                return False

    return True
