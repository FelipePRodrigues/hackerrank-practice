# def appendAndDelete(s, t, k):
#     equal_size = 0

#     for letter_idx in range(len(desired)):
#         try:
#             if t[letter_idx] == s[letter_idx]:
#                 equal_size += 1
#             else:
#                 break
#         except:
#             break

#     if k == (len(s) + len(desired) - equal_size * 2):
#         return "Yes"

#     if k > len(s) + len(desired):
#         return "Yes"

#     if k % (len(desired) - len(s)) == 0:
#         return "Yes"

#     return "No"


def appendAndDelete(initial, desired, operations):
    c = 0
    length = len(initial)

    while initial[:length] != desired[:length]:
        length -= 1
        c += 1

    o = ((len(desired)-length)+c)

    if operations < o:
        return "No"
    elif (len(initial)+len(desired)) <= operations:
        return "Yes"
    elif 2*len(desired) < operations:
        return "Yes"
    elif operations % 2 == o % 2:
        return "Yes"
    else:
        return "No"
