def pageCount(pageNumber, pageWanted):
    return min(pageWanted // 2, pageNumber//2 - pageWanted//2)
