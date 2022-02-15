def dayOfProgrammer(year):
    dopDate = ''

    if year <= 1917:
        leapYear = True if year % 4 == 0 else False
        dopDate = '{0}.09.{1}'.format(12 if leapYear else 13, year)
    elif year == 1918:
        dopDate = '26.09.1918'
    else:
        leapYear = True if year % 400 == 0 or (
            year % 4 == 0 and not year % 100 == 0) else False
        dopDate = '{0}.09.{1}'.format(12 if leapYear else 13, year)

    return dopDate
