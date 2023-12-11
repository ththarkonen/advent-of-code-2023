
import galaxies
import numpy as np

file = open("./day11/data.txt")
lines = file.readlines()

galaxiesII, galaxiesJJ = galaxies.parse( lines, rate = 2)
galaxiesLargeII, galaxiesLargeJJ = galaxies.parse( lines, rate = 1000000)

distances = galaxies.computeDistances( galaxiesII, galaxiesJJ)
distancesLong = galaxies.computeDistances( galaxiesLargeII, galaxiesLargeJJ)

totalDistance = sum( distances )
totalDistanceLong = sum( distancesLong )

print( totalDistance )
print( totalDistanceLong )