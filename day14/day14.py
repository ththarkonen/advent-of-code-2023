
import rocks
import json

file = open("./day14/data.txt")
lines = file.readlines()

rockObject = rocks.parse( lines )

simulationCycles = 125
directions = ["north", "west", "south", "east"]

loadPart1 = 0
totalLoads = []

historyFilePath = "./day14/loads.json"

if False:
    part1 = True
    for ii in range( simulationCycles ):
        for direction in directions:
            rockObject = rocks.turn( rockObject, direction)

            if part1: loadPart1 = rocks.computeLoad( rockObject, "north")
            part1 = False

        loadII = rocks.computeLoad( rockObject, "north")
        totalLoads.append( loadII )
        print( ii, loadII )
        
        with open( historyFilePath, "w") as f:
            json.dump( totalLoads, f)

totalCycles = 1000000000
loadPart2 = rocks.computeFinalLoad( "./day14/loads.json", totalCycles)

print( loadPart1 )
print( loadPart2 )