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
