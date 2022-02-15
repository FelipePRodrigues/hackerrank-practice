def migratoryBirds(birds):
    groupedBirds = {}

    for bird in birds:
        if bird in groupedBirds:
            groupedBirds[bird] += 1
        else:
            groupedBirds[bird] = 1

    birdId = 0
    birdCount = 0
    for bird in groupedBirds:
        if groupedBirds[bird] > birdCount:
            birdCount = groupedBirds[bird]
            birdId = bird

        if groupedBirds[bird] == birdCount and bird < birdId:
            birdId = bird

    return birdId
