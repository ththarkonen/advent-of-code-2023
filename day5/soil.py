
def parseMaps( lines ):

    seeds = []
    maps = {}

    destinationName = ""
    sourceName = ""

    for line in lines:
        
        line = line.replace("\n", "")
        if line == "":
            
            if sourceName != "": maps[ sourceName ] = map

            continue

        if "seeds" in line:

            line = line.split(":")[1]
            seeds = line.split(" ")

            seeds = [ int(seed) for seed in seeds if seed != ""]
            continue

        if "map" in line:

            line = line.split(" ")[0]
            line = line.split("-to-")
            
            destinationName = line[1]
            sourceName = line[0]

            map = {}
            map["destination"] = destinationName
            map["source"] = sourceName
            map["mappings"] = []

            continue

        numbers = line.split(" ")
        numbers = [ int( number ) for number in numbers]

        minDestination = numbers[0]
        minSource = numbers[1]
        step = numbers[2]

        maxDestination = minDestination + step - 1
        maxSource = minSource + step - 1

        mapping = {}
        mapping["destination"] = {}
        mapping["source"] = {}

        mapping["destination"]["min"] = minDestination
        mapping["destination"]["max"] = maxDestination

        mapping["source"]["min"] = minSource
        mapping["source"]["max"] = maxSource

        map["mappings"].append( mapping )

    maps[ sourceName ] = map
    return seeds, maps


def computeSeedRanges( seeds ):

    nSeeds = len( seeds )
    seedRanges = []

    for ii in range( 0, nSeeds, 2):
        
        step = seeds[ ii + 1 ]
        
        minIndex = seeds[ii]
        maxIndex = minIndex + step - 1

        seedRanges.append( minIndex )
        seedRanges.append( maxIndex )

    seedRanges = sorted( seedRanges )
    return seedRanges


def computeMapping( state, mappings):

    for mapping in mappings:

        minSource = mapping["source"]["min"]
        maxSource = mapping["source"]["max"]

        if state < minSource or maxSource < state: continue

        shift = state - minSource
        return mapping["destination"]["min"] + shift

    return state


def addCut( seedRange, mappings):
            
    seedMin = seedRange[0]
    seedMax = seedRange[1]

    if seedMin == seedMax:

        wasCut = False
        newSeedRanges = [ seedMin, seedMax]
        return ( newSeedRanges, wasCut)

    for mapping in mappings:

        minSource = mapping["source"]["min"]
        maxSource = mapping["source"]["max"]

        if seedMin == minSource and seedMax == maxSource:

            wasCut = False
            newSeedRanges = [ seedMin, seedMax]
            return ( newSeedRanges, wasCut)

        if seedMin == minSource and seedMax > maxSource:

            wasCut = True
            newSeedRanges = [ seedMin, maxSource, maxSource + 1, seedMax]
            return ( newSeedRanges, wasCut)

        if seedMax == maxSource and seedMin < minSource:

            wasCut = True
            newSeedRanges = [ seedMin, minSource - 1, minSource, maxSource]
            return ( newSeedRanges, wasCut)
        
        if seedMax == minSource:

            wasCut = True
            newSeedRanges = [ seedMin, minSource - 1, minSource, minSource]
            return ( newSeedRanges, wasCut)
        
        if seedMin == maxSource:

            wasCut = True
            newSeedRanges = [ maxSource, maxSource, maxSource + 1, seedMax]
            return ( newSeedRanges, wasCut)

        if seedMin < minSource and seedMax < maxSource and seedMax > minSource:

            wasCut = True
            newSeedRanges = [ seedMin, minSource - 1, minSource, seedMax]
            return ( newSeedRanges, wasCut)

        if seedMin > minSource and seedMax > maxSource and seedMin < maxSource:

            wasCut = True
            newSeedRanges = [ seedMin, maxSource, maxSource + 1, seedMax]
            return ( newSeedRanges, wasCut)

        if seedMin < minSource and seedMax > maxSource:

            wasCut = True
            newSeedRanges = [ seedMin, minSource - 1, minSource, maxSource, maxSource + 1, seedMax]
            return ( newSeedRanges, wasCut)

    wasCut = False
    newSeedRanges = [ seedMin, seedMax]
    return ( newSeedRanges, wasCut)


def computeNewSeedRanges( seedRanges, mappings):

    nSeedRanges = len( seedRanges )
    newCuts = True

    while newCuts:

        newSeedRanges = []
        newCuts = False

        for ii in range( 0, nSeedRanges, 2):

            seedRange = seedRanges[ii:(ii+2)]

            newRanges, wasCut = addCut( seedRange, mappings)
            if wasCut: newCuts = True

            newSeedRanges = newSeedRanges + newRanges

        seedRanges = newSeedRanges
        nSeedRanges = len( seedRanges )

    return newSeedRanges


def computeSeedRangeInfo( seedRanges, maps):

    states = seedRanges.copy()
    source = "seed"

    infos = {}
    infos["seeds"] = seedRanges

    while source != "location":

        map = maps[ source ]
        destination = map["destination"]
        mappings = map["mappings"]

        states = computeNewSeedRanges( states, mappings)

        for ii, state in enumerate( states ):
            states[ii] = computeMapping( state, mappings)

        infos[ destination ] = states.copy()
        source = destination

    return infos


def computeSeedInfo( seeds, maps):

    states = seeds.copy()
    source = "seed"

    infos = {}
    infos["seeds"] = seeds

    while source != "location":

        map = maps[ source ]
        destination = map["destination"]
        mappings = map["mappings"]

        for ii, state in enumerate( states ):
            states[ii] = computeMapping( state, mappings)

        infos[ destination ] = states.copy()
        source = destination

    return infos
