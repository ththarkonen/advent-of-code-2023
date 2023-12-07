
from collections import Counter

points = {"A": 14,
          "K": 13,
          "Q": 12,
          "J": 11,
          "T": 10,
          "9": 9,
          "8": 8,
          "7": 7,
          "6": 6,
          "5": 5,
          "4": 4,
          "3": 3,
          "2": 2}

pointsJoker = {"A": 14,
          "K": 13,
          "Q": 12,
          "J": 1,
          "T": 10,
          "9": 9,
          "8": 8,
          "7": 7,
          "6": 6,
          "5": 5,
          "4": 4,
          "3": 3,
          "2": 2,
          "2": 2}

def parseHands( lines ):

    hands = []
    bids = []

    for line in lines:

        line = line.replace("\n","").split()

        handString = line[0]
        handCounts = Counter( handString )

        hand = {}
        hand["cards"] = handString
        hand["counts"] = handCounts

        bid = line[1]
        bid = int( bid )

        hands.append( hand )
        bids.append( bid )

    return hands, bids


def computeHandType( hand ):

    cardCounts = hand["counts"]

    isFiveOK = False
    isFourOK = False
    hasThreeOK = False
    hasPairOK = False
    totalPairs = 0

    for _, count in cardCounts.items():
        if count == 5: isFiveOK = True
        if count == 4: isFourOK = True
        if count == 3: hasThreeOK = True
        if count == 2:
            totalPairs += 1
            hasPairOK = True

    if isFiveOK: return 7
    if isFourOK: return 6
    if hasThreeOK and hasPairOK: return 5
    if hasThreeOK: return 4
    if totalPairs == 2: return 3
    if hasPairOK:  return 2
    return 1


def computeHandTypeWithJoker( hand ):

    cardCounts = hand["counts"]

    isFiveOK = False
    isFourOK = False
    hasThreeOK = False
    hasPairOK = False
    jokerCount = 0
    totalPairs = 0

    for card, count in cardCounts.items():
        if count == 5: isFiveOK = True
        if count == 4: isFourOK = True
        if count == 3: hasThreeOK = True
        if count == 2:
            totalPairs += 1
            hasPairOK = True

        if card == "J": jokerCount += count

    if isFiveOK: return 7
    if isFourOK and jokerCount == 4: return 7
    if isFourOK and jokerCount == 1: return 7
    if hasThreeOK and jokerCount == 2: return 7
    if hasPairOK and jokerCount == 3: return 7

    if isFourOK and jokerCount == 0: return 6
    if hasThreeOK and jokerCount == 1: return 6
    if hasThreeOK and jokerCount == 3 and totalPairs <= 1: return 6 
    if hasPairOK and jokerCount == 2 and totalPairs == 2: return 6

    if hasThreeOK and hasPairOK: return 5
    if hasThreeOK and jokerCount == 1: return 5
    if totalPairs == 2 and jokerCount == 1: return 5

    if hasThreeOK: return 4
    if hasPairOK and jokerCount == 1: return 4
    if jokerCount == 2: return 4

    if totalPairs == 2: return 3
    if hasPairOK: return 2
    if jokerCount == 1: return 2

    return 1


def computeTotalWinnings( hands, bids, withJoker = False):

    handStrengths = []

    for hand in hands:

        cardStrengths = 0
        power = 5

        for ii, card in enumerate( hand["cards"] ):

            factor = 10 ** ( 2 * power - 2 * ii ) / 14

            if withJoker:
                cardStrengths += factor * pointsJoker[card]
            else:
                cardStrengths += factor * points[card]

        if withJoker:
            typePoints =  computeHandTypeWithJoker( hand )
        else:
            typePoints =  computeHandType( hand )

        factor = 10 ** ( 2 * power + 1 )
        strength = cardStrengths + factor * typePoints
        handStrengths.append( strength )

    hbh = zip( hands, bids, handStrengths)
    hbh = sorted( hbh, key = lambda x: x[2])

    winnings = []

    for ii, x in enumerate( hbh ):
        win = (ii + 1) * x[1]
        winnings.append( win )

    totalWinnings = sum( winnings )
    return totalWinnings
