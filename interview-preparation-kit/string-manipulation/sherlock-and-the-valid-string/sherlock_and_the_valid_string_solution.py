def isValid(string):
    string_list = list(string)

    indexes = {}
    values = []

    for char in string_list:
        if char in indexes:
            values[indexes[char]] += 1
        else:
            values.append(1)
            indexes[char] = len(values) - 1

    max_value = max(values)
    min_value = min(values)

    max_values = values.count(max_value)
    min_values = values.count(min_value)

    if min_value == max_value:
        return 'YES'

    if min_value == 1 and min_values == 1 and len(set(values)) == 2:
        return 'YES'

    if abs(max_value - min_value) == 1 and min_values == 1:
        return 'YES'

    if abs(max_value - min_value) == 1 and max_values == 1:
        return 'YES'

    return 'NO'

print(isValid('aaaaabc')) # NO
print(isValid('abcdefghhgfedecba')) # YES
print(isValid('xxxaabbccrry')) # NO
