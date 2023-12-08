
import ghosts

file = open("./day8/data.txt")
lines = file.readlines()

directions, nodes = ghosts.parseMap( lines )
startingNodes = ghosts.parseStartingNodes( nodes )

currentNode = "AAA"
steps = ghosts.traverseNodes( currentNode, directions, nodes)

parallelMinimumSteps = []

for startingNode in startingNodes:
    minSteps = ghosts.traverseNodes( startingNode, directions, nodes, parallelMoves = True)
    parallelMinimumSteps.append( minSteps )

totalSteps = ghosts.computeTotalSteps( parallelMinimumSteps )

print( steps )
print( totalSteps )