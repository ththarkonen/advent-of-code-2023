
numberStrings = {}
numberStrings["one"] = "1"
numberStrings["two"] = "2"
numberStrings["three"] = "3"
numberStrings["four"] = "4"
numberStrings["five"] = "5"
numberStrings["six"] = "6"
numberStrings["seven"] = "7"
numberStrings["eight"] = "8"
numberStrings["nine"] = "9"

def parseDataPart1( lines ):

    numbers = []

    for line in lines:

        number = ""
        line = line.replace("\n","")

        for character in line:
            if character.isdigit():
                number = number + character

        number = number[0] + number[-1]
        number = int( number )
        numbers.append( number )

    return numbers

def parseDataPart2( lines ):

    numbers = []

    for line in lines:

        number = ""
        line = line.replace("\n","")
            
        nCharacters = len( line )
        for ii in range( nCharacters ):

            character = line[ii]
            if character.isdigit():
                number = number + character
                continue

            for key in numberStrings:
                
                nKey = len( key )
                if nCharacters - ii >= nKey:

                    startIndex = ii
                    stopIndex = ii + nKey
                    substring = line[ startIndex : stopIndex ]
                    
                    if substring == key:
                        number = number + numberStrings[key]
                        continue

        number = number[0] + number[-1]
        number = int( number )
        numbers.append( number )

    return numbers

def totalCalibrationValue( calibrationValues ):

    total = 0
    for value in calibrationValues:
        total = total + value

    return total