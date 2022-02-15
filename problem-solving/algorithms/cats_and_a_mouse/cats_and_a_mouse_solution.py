def catAndMouse(aCat, bCat, cMouse):
    aCatDistance = (aCat - cMouse) if aCat > cMouse else (cMouse - aCat)
    bCatDistance = (bCat - cMouse) if bCat > cMouse else (cMouse - bCat)

    if aCatDistance == bCatDistance:
        return 'Mouse C'
    else:
        return 'Cat {}'.format('A' if aCatDistance < bCatDistance else 'B')
