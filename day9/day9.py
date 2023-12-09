
import numpy as np
import oasis

file = open("./day9/data.txt")
lines = file.readlines()

histories = oasis.parseHistories( lines )
flipHistories = np.flip( histories )

exptrapolations = oasis.extrapolateHistories( histories )
exptrapolationsBack = oasis.extrapolateHistories( flipHistories )

totalPart1 = sum( exptrapolations )
totalPart2 = sum( exptrapolationsBack )

print( totalPart1 )
print( totalPart2 )