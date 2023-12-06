
import soil

file = open("./day5/data.txt")
lines = file.readlines()

seeds, maps = soil.parseMaps( lines )
seedRanges = soil.computeSeedRanges( seeds )

infos = soil.computeSeedInfo( seeds, maps)
rangeInfos = soil.computeSeedRangeInfo( seedRanges, maps)

minLocation = min( infos["location"] )
altMinLocation = min( rangeInfos["location"] )

print( minLocation )
print( altMinLocation )
