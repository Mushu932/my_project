students = [
    {
        "name": "Анна",
        "age": 20,
        "grades": [5, 4, 5, 4, 5]
    },
    {
        "name": "Борис",
        "age": 21,
        "grades": [3, 4, 4, 3, 5]
    },
    {
        "name": "Виктор",
        "age": 19,
        "grades": [5, 5, 4, 5, 5]
    }
]

for student in students:
    name = student["name"]
    grades = student["grades"]

    total = 0
    count = 0
    for grade in grades:
        total += grade
        count += 1

    average = total / count

    print(f"Студент: {name}, средняя оценка: {average}")