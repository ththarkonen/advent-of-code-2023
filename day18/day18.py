
import lava

file = open("./day18/data.txt")
lines = file.readlines()

trench, nSpots = lava.parse( lines )
trenchCorrect, nSpotsCorrect = lava.parseHex( lines )

area = lava.calculateArea( trench, nSpots)
areaCorrect = lava.calculateArea( trenchCorrect, nSpotsCorrect)

print( area )
print( areaCorrect )