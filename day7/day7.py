
import camelCards

file = open("./day7/data.txt")
lines = file.readlines()

hands, bids = camelCards.parseHands( lines )
totalWinnings = camelCards.computeTotalWinnings( hands, bids)
totalWinningsJoker = camelCards.computeTotalWinnings( hands, bids, withJoker = True)

print( totalWinnings )
print( totalWinningsJoker )