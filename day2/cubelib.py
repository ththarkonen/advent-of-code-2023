
def parseData( lines ):

    cubeGames = []

    for line in lines:

        cubeGame = {}

        line = line.replace("\n", "")
        line = line.split(":")

        id = line[0].split(" ")[1]
        subgames = line[1].split(";")

        cubeGame["id"] = int( id )
        cubeGame["cubeSets"] = []

        for subgame in subgames:

            cubeSet = {}
            cubes = subgame.split(",")

            for coloredCube in cubes:

                coloredCube = coloredCube.split(" ")

                nCubes = coloredCube[1]
                cubeColor = coloredCube[2]

                cubeSet[ cubeColor ] = int( nCubes )

            cubeGame["cubeSets"].append( cubeSet )

        cubeGames.append( cubeGame )

    return cubeGames

def getPossibleGames( games, cubeLimits):

    possibleGames = []

    for game in games:

        possible = True

        for subgame in game["cubeSets"]:
            for color in cubeLimits:

                if color not in subgame: continue
                if subgame[color] > cubeLimits[color]: possible = False

        if possible: possibleGames.append( game )

    return possibleGames

def getMinimumCubesNeeded( games ):
    
    minimums = []

    for game in games:

        minimumCubes = {}

        for subgame in game["cubeSets"]:
            for color in subgame:

                if color not in minimumCubes:

                    minimumCubes[color] = subgame[color]
                    continue

                if minimumCubes[color] < subgame[color]:
                    minimumCubes[color] = subgame[color]

        minimums.append( minimumCubes )

    return minimums

def computeGamePower( minimums ):

    gamePowers = []

    for minimumCubes in minimums:

        power = 1
        for color in minimumCubes:
            power = power * minimumCubes[color]

        gamePowers.append( power )

    return gamePowers