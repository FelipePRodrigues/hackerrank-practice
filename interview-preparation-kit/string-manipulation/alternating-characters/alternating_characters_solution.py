def alternatingCharacters(string):
    deleted = 0
    string_list = list(string)

    for idx, char in enumerate(string_list):
        if idx + 1 < len(string_list) and char == string_list[idx + 1]:
            deleted += 1

    return deleted