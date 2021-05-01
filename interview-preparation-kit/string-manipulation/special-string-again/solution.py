# import math


# def substrCount(length, string):
#     string_list = list(string)
#     total = list(string_list)

#     for idx, char in enumerate(string_list):

#         if not len(string_list) < idx + 1:
#             next_letters = list(string_list[idx + 1:])

#         test = char
#         for next_letter in next_letters:
#             test += next_letter

#             if not isPossibleSpecialString(test):
#                 break

#             if checkSpecialString(list(test)):
#                 total.append(test)

#     return len(total)


# def isPossibleSpecialString(string):
#     if len(set(string)) <= 2:
#         return True


# def checkSpecialString(string):
#     if len(set(string)) == 1:
#         return True

#     if len(string) % 2 != 0:
#         string.remove(string[math.floor(len(string) / 2)])

#         if len(set(string)) == 1:
#             return True

#     return False


def substrCount(n, string):
    total = 0
    count_sequence = 0
    previous = ''
    for i, v in enumerate(string):
        # first increase counter for all seperate characters
        count_sequence += 1
        if i and (previous != v):
            # if this is not the first char in the string
            # and it is not same as previous char,
            # we should check for sequence x.x, xx.xx, xxx.xxx etc
            # and we know it cant be longer on the right side than
            # the sequence we already found on the left side.
            j = 1
            while ((i-j) >= 0) and ((i+j) < len(string)) and j <= count_sequence:
                # make sure the chars to the right and left are equal
                # to the char in the previous found squence
                if string[i-j] == previous == string[i+j]:
                    # if so increase total score and step one step further out
                    total += 1
                    j += 1
                else:
                    # no need to loop any further if this loop did
                    # not find an x.x  pattern
                    break
            #if the current char is different from previous, reset counter to 1
            count_sequence = 1
        total += count_sequence
        previous = v
    return total


print(substrCount(5, 'asasd')) # 7
print(substrCount(7, 'abcbaba')) # 10
print(substrCount(4, 'aaaa')) # 10