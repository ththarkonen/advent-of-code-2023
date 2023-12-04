
def parseLotteryNumbers( lines ):

    winningNumbers = []
    lotteryNumbers = []

    for line in lines:

        winningNumbersLine = []
        lotteryNumbersLine = []

        line = line.replace("\n", "")
        line = line.split(":")
        line = line[1].split("|")
        
        winningStrings = line[0].split(" ")
        lotteryStrings = line[1].split(" ")

        for win in winningStrings:
            if win == "": continue
            
            winNumber = int( win )
            winningNumbersLine.append( winNumber )

        for lot in lotteryStrings:
            if lot == "": continue

            lotNumber = int( lot )
            lotteryNumbersLine.append( lotNumber )

        winningNumbers.append( winningNumbersLine )
        lotteryNumbers.append( lotteryNumbersLine )

    return ( winningNumbers, lotteryNumbers)


def computePoints( numbersList, winningNumbersList):

    points = []
    matches = []

    nLotteries = len( numbersList )
    
    for ii in range( nLotteries ):

        numbersII = numbersList[ii]
        winningNumberII = winningNumbersList[ii]

        pointsII = 1
        matchesII = 0

        for number in numbersII:
            if number not in winningNumberII: continue
                
            pointsII = 2 * pointsII
            matchesII = matchesII + 1

        pointsII = 0.5 * pointsII
        pointsII = int( pointsII )

        points.append( pointsII )
        matches.append( matchesII )

    return points, matches


def copyCards( points ):

    nCards = len( points )
    maxStopIndex = nCards

    totalCards = nCards * [ 1 ]
    cardGenerator = {}

    for ii, pointsII in enumerate( points ):
        if pointsII == 0: continue

        startIndex = ii + 1
        stopIndex = min( startIndex + pointsII, maxStopIndex)

        cardGenerator[ii] = [ *range( startIndex, stopIndex) ]

    for ii, copyInds in cardGenerator.items():
        for ind in copyInds: totalCards[ind] += totalCards[ii]

    return totalCards
    