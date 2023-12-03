
def saveNumber( number, numberInds, numbers):

    if number == "": return numbers

    numberTuple = ( int( number ), numberInds)
    numbers.append( numberTuple )

    return numbers

def parseSchematic( lines ):

    numbers = []
    symbols = {}

    ii = 0
    for line in lines:

        line = line.replace("\n","")

        number = ""
        numberInds = []
        previousWasNumber = True

        nCharacters = len( line )
        for jj in range( nCharacters ):

            c = line[jj]

            if c == ".":
                previousWasNumber = False
                numbers = saveNumber( number, numberInds, numbers)
                number = ""
                continue

            if not c.isdigit() and c != ".":

                symbolInds = ( ii, jj)

                if c not in symbols: symbols[c] = [ symbolInds ]
                else: symbols[c].append( symbolInds )

                previousWasNumber = False
                numbers = saveNumber( number, numberInds, numbers)
                number = ""
                continue

            if c.isdigit() and not previousWasNumber:
                
                previousWasNumber = True

                number = c
                numberInds = [ ( ii, jj) ]
                continue

            if c.isdigit() and previousWasNumber:

                previousWasNumber = True

                number = number + c
                numberInds.append( ( ii, jj) )
                continue

        numbers = saveNumber( number, numberInds, numbers)
        ii = ii + 1
    
    return ( numbers, symbols)

def checkIfPartNumber( numberTuple, symbols, directions):

        numberValue = numberTuple[0]
        numberInds = numberTuple[1]

        for symbol in symbols:
            for inds in symbols[symbol]:
                for dir in directions:

                    nextII = inds[0] + dir[0]
                    nextJJ = inds[1] + dir[1]
                    nextInds = ( nextII, nextJJ)

                    if nextInds in numberInds: return numberValue

        return None

def getPartNumbers( numbers, symbols):

    partNumbers = []
    directions = [( 0, 1),
                  (-1, 1),
                  (-1, 0),
                  (-1,-1),
                  ( 0,-1),
                  ( 1,-1),
                  ( 1, 0),
                  ( 1, 1)]

    for numberTuple in numbers:

        partNumber = checkIfPartNumber( numberTuple, symbols, directions)

        if partNumber is not None: partNumbers.append( partNumber )

    return partNumbers

def getGearRatios( numbers, symbols):

    gearSymbolInds = symbols["*"]
    tempGearSymbol = {"*": []}

    gearRatios = []
    directions = [( 0, 1),
                  (-1, 1),
                  (-1, 0),
                  (-1,-1),
                  ( 0,-1),
                  ( 1,-1),
                  ( 1, 0),
                  ( 1, 1)]
    
    for inds in gearSymbolInds:
        
        gearNumbers = []
        tempGearSymbol["*"] = [ inds ]

        for numberTuple in numbers:

            gearNumber = checkIfPartNumber( numberTuple, tempGearSymbol, directions)

            if gearNumber is not None: gearNumbers.append( gearNumber )

        nPossibleGearNumbers = len( gearNumbers )

        if nPossibleGearNumbers != 2: continue

        gearRatio = gearNumbers[0] * gearNumbers[1]
        gearRatios.append( gearRatio )

    return gearRatios
