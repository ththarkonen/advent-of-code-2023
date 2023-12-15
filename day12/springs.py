
import re
import math

def parse( lines ):

    symbolList = []
    altSymbolList = []
    numberList = []

    for line in lines:

        line = line.replace("\n","").split()

        symbols = line[0]

        while ".." in symbols:
            symbols = symbols.replace("..", ".")

        originalSymbols = symbols
        symbols = symbols.replace("?","#")

        numbers = line[1].split(",")
        numbers = [ int(x) for x in numbers ]

        symbolList.append( originalSymbols )
        altSymbolList.append( symbols )
        numberList.append( numbers )

    return symbolList, altSymbolList, numberList


def fold( symbols, altSymbols, numbers):

    symbolsFoldedList = []
    altSymbolsFoldedList = []
    numbersFoldedList = []

    nRows = len( symbols )

    for ii in range( nRows ):

        symbolsFolded = ""
        altSymbolsFolded = ""
        numbersFolded = []

        symbolsII = symbols[ii]
        altSymbolsII = altSymbols[ii]
        numbersII = numbers[ii]

        for _ in range(5):

            symbolsFolded += symbolsII + "?"
            altSymbolsFolded += altSymbolsII + "#"
            numbersFolded = numbersFolded + numbersII

        symbolsFolded = symbolsFolded[:-1]
        altSymbolsFolded = altSymbolsFolded[:-1]

        symbolsFoldedList.append( symbolsFolded )
        altSymbolsFoldedList.append( altSymbolsFolded )
        numbersFoldedList.append( numbersFolded )

    return symbolsFoldedList, altSymbolsFoldedList, numbersFoldedList


def findPatternInds( altSymbols, number):
    
    tempString = "(?="
    for _ in range( number ):
        tempString += "#"

    tempString += ")"
    inds = [m.start() for m in re.finditer( tempString, altSymbols)]

    return inds


def countLocations( symbols, altSymbols, number):
    
    patternStartInds = findPatternInds( altSymbols, number)
        
    total = 0
    for ii in patternStartInds:

        checkInd = ii + number
        symbolsBefore = symbols[:ii]
        if "#" in symbolsBefore: continue
        if "#" not in symbols[checkInd:]: total = total + 1

    return total


def getCombinations( symbols, altSymbols, numbers):

    total = 0
    nNumbers = len( numbers )

    if nNumbers >= 3:

        midNumberInd = math.floor ( 0.5 * nNumbers )
        midNumberInd = int( midNumberInd )
        midNumber = numbers[ midNumberInd ]

        patternStartInds = findPatternInds( altSymbols, midNumber)
        
        total = 0

        for ii in patternStartInds:

            checkInd = ii + midNumber

            symbolsBefore = symbols[:ii]
            altSymbolsBefore = altSymbols[:ii]
            numbersBefore = numbers[:midNumberInd]

            symbolsAfter = symbols[checkInd:]
            altSymbolsAfter = altSymbols[checkInd:]
            numbersAfter = numbers[midNumberInd+1:]

            totalNumbersBefore = sum( numbersBefore )
            totalNumbersAfter = sum( numbersAfter )

            nHashesBefore = len( altSymbolsBefore.replace(".","") )
            nHashesAfter = len( altSymbolsAfter.replace(".","") )

            if nHashesBefore < totalNumbersBefore: continue
            if nHashesAfter < totalNumbersAfter: continue

            if symbolsBefore[-1] == "#": continue
            if symbolsAfter[0] == "#": continue

            if symbolsBefore[-1] == "?":
                symbolsBefore = symbolsBefore[:-1]
                altSymbolsBefore = altSymbolsBefore[:-1]
            elif symbolsBefore[-1] == ".":
                symbolsBefore = symbolsBefore[:-1]
                altSymbolsBefore = altSymbolsBefore[:-1]

            if symbolsAfter[0] == "?":
                symbolsAfter = symbolsAfter[1:]
                altSymbolsAfter = altSymbolsAfter[1:]
            elif symbolsAfter[0] == ".":
                symbolsAfter = symbolsAfter[1:]
                altSymbolsAfter = altSymbolsAfter[1:]

            nNumbersBefore = len( numbersBefore )
            nNumbersAfter = len( numbersAfter )

            totalNumbersBefore = sum( numbersBefore )
            totalNumbersAfter = sum( numbersAfter )

            spaceBefore = len( altSymbolsBefore )
            spaceNeededBefore = totalNumbersBefore + nNumbersBefore - 1

            spaceAfter = len( altSymbolsAfter )
            spaceNeededAfter = totalNumbersAfter + nNumbersAfter - 1

            if spaceBefore < spaceNeededBefore: continue
            if spaceAfter < spaceNeededAfter: continue
            
            totalBefore = getCombinations( symbolsBefore, altSymbolsBefore, numbersBefore)
            if totalBefore == 0: continue

            totalAfter = getCombinations( symbolsAfter, altSymbolsAfter, numbersAfter)
            if totalAfter == 0: continue

            total = total + totalBefore * totalAfter

        return total

    if nNumbers == 0: return 0

    nNumbers = len( numbers )
    nSymbols = len( symbols )

    currentNumber = numbers[0]
    nextNumbers = numbers[1:]
    nNextNumbers = len( numbers )

    if nNumbers == 1:
        total = countLocations( symbols, altSymbols, currentNumber)
        return total

    patternStartInds = findPatternInds( altSymbols, currentNumber)

    for ii in patternStartInds:

        checkInd = ii + currentNumber
        startInd = ii
        cutInd = ii + currentNumber + 1

        symbolsBefore = symbols[:startInd]

        if checkInd > nSymbols - 1: pass
        elif "#" in symbolsBefore: continue
        elif symbols[checkInd] == "#": continue

        cutSymbols = symbols[cutInd:]
        cutAltSymbols = altSymbols[ cutInd:]

        if nNextNumbers == 1 and "#" not in cutSymbols:
            
            patternStartInds = findPatternInds( cutAltSymbols, currentNumber)
            total = total + len( patternStartInds )
        else:
            total = total + getCombinations( cutSymbols, cutAltSymbols, nextNumbers)
    
    return total


def computePossibleCombinations( symbols, altSymbols, numbers):
    return getCombinations( symbols, altSymbols, numbers)



