def pickingNumbers(a):
    numbers = sorted(list(set(a)))
    maximum = a.count(numbers[0])

    for number in numbers[1:]:
        total = a.count(number) + a.count(number-1)

        if total > maximum:
            maximum = total

    return maximum


print(pickingNumbers([4, 4, 4, 4, 1, 1, 2, 2, 2]))  # 5
print(pickingNumbers([1, 2, 4, 4, 1, 1, 2, 6, 6, 5, 5]))  # 6
print(pickingNumbers([4, 6, 5, 3, 3, 1]))  # 3
print(pickingNumbers([1, 2, 2, 3, 1, 2]))  # 5
