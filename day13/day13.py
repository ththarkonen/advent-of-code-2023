
import mirrors

file = open("./day13/data.txt")
lines = file.readlines()

patterns = mirrors.parse( lines )

verticalReflections = mirrors.computeReflections( patterns, mode = "vertical")
horizontalReflections = mirrors.computeReflections( patterns, mode = "horizontal")

verticalReflectionsSmudge = mirrors.computeReflections( patterns, mode = "vertical", cleanMode = "smudge")
horizontalReflectionsSmudge = mirrors.computeReflections( patterns, mode = "horizontal", cleanMode = "smudge")

total = sum( verticalReflections ) + 100 * sum( horizontalReflections )
totalSmudge = sum( verticalReflectionsSmudge ) + 100 * sum( horizontalReflectionsSmudge )

print( total )
print( totalSmudge )