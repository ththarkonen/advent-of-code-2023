
def parse( lines ):

    sequences = []

    for line in lines:

        line = line.replace("\n", "")
        line = line.split(",")

        for subline in line:
            sequences.append( subline )

    return sequences

def HASH( sequence ):

    value = 0

    for c in sequence:

        asciiCode = ord( c )
        value = value + asciiCode
        value = 17 * value
        value = value % 256

    return value

def constructLenses( sequences ):

    lenses = []
    nLenses = len( sequences )

    for ii in range( nLenses ):

        lens = {}

        if "=" in sequences[ii]:

            lens["type"] = "="
            focalLength = sequences[ii].split("=")[1]
            focalLength = int( focalLength )

            lens["label"] = sequences[ii][:-2]
            lens["boxID"] = HASH( lens["label"] )
            lens["focalLength"] = focalLength
        else:

            lens["type"] = "-"
            lens["label"] = sequences[ii][:-1]
            lens["boxID"] = HASH( lens["label"] )

        lenses.append( lens )
    
    return lenses


def removeLens( boxes, lens):

    boxID = lens["boxID"]
    label = lens["label"]

    box = boxes[ boxID ]

    for boxLens in box["lenses"]:
        if boxLens["label"] == label:
            boxes[ boxID ]["lenses"].remove( boxLens )
            return boxes
        
    return boxes


def addLens( boxes, lens):

    boxID = lens["boxID"]
    label = lens["label"]

    box = boxes[ boxID ]

    for lensIndex, boxLens in enumerate( box["lenses"] ):
        if boxLens["label"] == label:
            boxes[ boxID ]["lenses"][ lensIndex ] = lens
            return boxes
        
    boxes[ boxID ]["lenses"].append( lens )
    return boxes


def makeBoxes( lenses ):

    boxes = {}

    for ii in range( 256 ):
        boxes[ii] = {}
        boxes[ii]["lenses"] = []

    for lens in lenses:

        if lens["type"] == "-": boxes = removeLens( boxes, lens)
        elif lens["type"] == "=": boxes = addLens( boxes, lens)

    return boxes


def filterBoxes( boxes ):

    nonEmptyBoxes = []

    for box in boxes.values():

        if len( box["lenses"] ) == 0: continue

        boxNumber = box["lenses"][0]["boxID"]

        nonEmptyBox = ( boxNumber, box)
        nonEmptyBoxes.append( nonEmptyBox )

    return nonEmptyBoxes


def computeFocusingPowers( boxes ):

    powers = []

    for box in boxes:

        boxID = box[0]
        box = box[1]

        power = 0

        for ii, lens in enumerate( box["lenses"] ):
            power = power + ( boxID + 1 ) * ( ii + 1 ) * lens["focalLength"]

        powers.append( power )

    return powers