def breakingRecords(scores):
    breakMin = 0
    breakMax = 0
    min = scores[0]
    max = scores[0]

    for score in scores:
        if score > max:
            breakMax += 1
            max = score

        if score < min:
            breakMin += 1
            min = score

    return [breakMax, breakMin]
