def makeAnagram(a, b):
    a = list(a)
    b = list(b)

    matches = 0
    bigger = a if len(a) > len(b) else b
    smaller = b if len(a) > len(b) else a

    for small_letter in smaller:
        if small_letter in bigger:
            matches += 1
            bigger.remove(small_letter)

    return len(bigger) + len(smaller) - matches
