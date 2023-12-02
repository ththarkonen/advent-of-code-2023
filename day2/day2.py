
import cubelib

file = open("./day2/data.txt")
lines = file.readlines()

cubeLimits = {}
cubeLimits["red"] = 12
cubeLimits["green"] = 13
cubeLimits["blue"] = 14

cubeGames = cubelib.parseData( lines )
possibleCubeGames = cubelib.getPossibleGames( cubeGames, cubeLimits)
minimumCubesNeeded = cubelib.getMinimumCubesNeeded( cubeGames )
gamePowers = cubelib.computeGamePower( minimumCubesNeeded )

totalID = 0
totalPower = 0

for possibleGame in possibleCubeGames:
    totalID = totalID + possibleGame["id"]

for gamePower in gamePowers:
    totalPower = totalPower + gamePower

print( totalID )
print( totalPower )