# ------------ Example 1 - Simple Dictionary ------------------------
dict1 = {
    "name": "Alex",
    "age": 13,
    "gpa": 3.9
}

print(dict1["name"])
print(dict1["age"])
print(dict1["gpa"])

gpa = dict1["gpa"]
print("GPA is", gpa)
print("\n\n")

# ------------ Example 2 - Dictionary with an Array -----------------
dict2 = {
    "name": "Alex",
    "age": 13,
    "gpa": 3.9,
    "classes": [
        "English",
        "Science",
        "PE",
        "Shop II",
        "Adv. Math",
    ]
}

classes = dict2["classes"]
for c in classes:
    print(c)

print("\n\n")

# ------- Example 3 - Dictionary with an Array of Dictionaries ------
dict3 = {
    "name": "Alex",
    "age": 13,
    "gpa": 3.9,
    "classes": [
        {
            "name": "English",
            "grade": 91.4,
            "letter_grade": "A-"
        },
        {
            "name": "Adv. Math",
            "grade": 88.2,
            "letter_grade": "B+"
        },
        {
            "name": "Shop II",
            "grade": 100.0,
            "letter_grade": "A"
        }
    ]
}

classes = dict3["classes"]
for c in classes:
    print(c["name"] + ": " + c["letter_grade"])

print("\nAlex's percentage in Shop II is:",
      dict3["classes"][2]["grade"])
