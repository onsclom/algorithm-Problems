def smallestDifference(arrayOne, arrayTwo):
    oneCur = 0
    twoCur = 0
    minDif = abs(arrayOne[0]-arrayTwo[0])
    minOne = 0
    minTwo = 0

    arrayOne.sort()
    arrayTwo.sort()

    while (oneCur < len(arrayOne) and twoCur < len(arrayTwo)):
        currentDif = abs(arrayOne[oneCur]-arrayTwo[twoCur])
        if currentDif < minDif:
            minDif = currentDif
            minOne = oneCur
            minTwo = twoCur

        if arrayOne[oneCur] < arrayTwo[twoCur]:
            oneCur += 1
        else:
            twoCur += 1

    return [arrayOne[minOne], arrayTwo[minTwo]]
