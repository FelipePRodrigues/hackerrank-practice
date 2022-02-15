def birthday(squares, sum, length):
    matches = 0

    for idx, numberInSquare in enumerate(squares):
        sequence = [numberInSquare]
        total = numberInSquare

        if len(sequence) == length and total == sum:
            matches += 1
            break
        else:
            newSquares = squares[(idx + 1):]

            for nextNumber in newSquares:
                sequence.append(nextNumber)
                total += nextNumber

                if len(sequence) == length and total == sum:
                    matches += 1
                    break
                elif len(sequence) >= length or total >= sum:
                    break

    print(matches)
    return matches
