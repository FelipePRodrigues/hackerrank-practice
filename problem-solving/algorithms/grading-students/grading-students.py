import math


def gradingStudents(grades):
    editedGrades = []

    for grade in grades:
        if grade >= 38:
            mod = (math.floor(grade / 5) + 1) * 5

            if mod - grade < 3:
                editedGrades.append(mod)
                continue

        editedGrades.append(grade)

    return editedGrades


TESTS = [
    [[73, 67, 38, 33], [75, 67, 40, 33]],
    [[72, 37, 40, 42], [72, 37, 40, 42]],
]

for test in TESTS:
    result = gradingStudents(test[0])

    if result == test[1]:
        print('Passed')
    else:
        print('Failed -> Received ' + str(result) +
              ' Expected ' + str(test[1]))
