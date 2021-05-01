def formingMagicSquare(matrix):
    possible_magic_squares = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
    ]

    totals = []
    for p in possible_magic_squares:
        total = 0
        for p_row, m_row in zip(p, matrix):
            for i, j in zip(p_row, m_row):
                if not i == j:
                    total += max([i, j]) - min([i, j])
        totals.append(total)
    return min(totals)
