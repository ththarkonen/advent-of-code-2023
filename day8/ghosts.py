
from collections import deque
import math

def parseMap( lines ):

    directions = []
    nodes = {}

    for character in lines[0]:
        if character == "R": directions.append("right")
        if character == "L": directions.append("left")

    for line in lines:

        if "=" not in line: continue

        line = line.replace("\n","")
        line = line.replace("(", "")
        line = line.replace(")", "")
        line = line.replace(",", "")
        line = line.replace("=", "")

        line = line.split()

        currentNode = line[0]
        leftNode = line[1]
        rightNode = line[2]

        nodes[ currentNode ] = {}
        nodes[ currentNode ]["left"] = leftNode
        nodes[ currentNode ]["right"] = rightNode
        
    directions = deque( directions )

    return directions, nodes

def traverseNodes( currentNode, directions, nodes, parallelMoves = False):

    if parallelMoves: stoppingCondition = currentNode[-1] == "Z"
    else: stoppingCondition = currentNode == "ZZZ"

    steps = 0
    while not stoppingCondition:

        dir = directions[0]
        currentNode = nodes[ currentNode ][dir]

        directions.rotate(-1)
        steps = steps + 1

        if parallelMoves: stoppingCondition = currentNode[-1] == "Z"
        else: stoppingCondition = currentNode == "ZZZ"

    return steps


def parseStartingNodes( nodes ):

    startingNodes = []

    for node in nodes:
        if node[-1] == "A": startingNodes.append( node )

    return startingNodes


def computeTotalSteps( minSteps ):

    totalSteps = 263

    for steps in minSteps:
        totalSteps = totalSteps * steps / 263

    return int( totalSteps )