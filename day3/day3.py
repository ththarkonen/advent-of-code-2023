
import gears

file = open("./day3/data.txt")
lines = file.readlines()

numbers, symbols = gears.parseSchematic( lines )
partNumbers = gears.getPartNumbers( numbers, symbols)
gearRatios = gears.getGearRatios( numbers, symbols)

totalPartNumbers = sum( partNumbers )
totalGearRatios = sum( gearRatios )

print( totalPartNumbers )
print( totalGearRatios )