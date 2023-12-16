
import hashing

file = open("./day15/data.txt")
lines = file.readlines()

sequences = hashing.parse( lines )
results = [ hashing.HASH( seq ) for seq in sequences]
totalResult = sum( results )

lenses = hashing.constructLenses( sequences )
boxes = hashing.makeBoxes( lenses )
nonEmptyBoxes = hashing.filterBoxes( boxes )

focusingPowers = hashing.computeFocusingPowers( nonEmptyBoxes )
totalFocusingPower = sum( focusingPowers )

print( totalResult )
print( totalFocusingPower )