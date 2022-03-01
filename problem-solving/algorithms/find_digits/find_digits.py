def findDigits(n):
    count = 0

    for digit in str(n):
        try:
            if n % int(digit) == 0:
                count = count + 1
        except:
            pass

    return count
