
import math

def parseRace( lines ):

    times = lines[0].replace("\n","")
    distances = lines[1].replace("\n","")

    times = times.split()[1:]
    distances = distances.split()[1:]

    nRaces = len( times )

    time = ""
    distance = ""

    for ii in range( nRaces ):

        time = time + times[ii]
        distance = distance + distances[ii]

    time = int( time )
    distance = int( distance )

    return ( [time], [distance])

def parseRaces( lines ):

    times = lines[0].replace("\n","")
    distances = lines[1].replace("\n","")

    times = times.split()[1:]
    distances = distances.split()[1:]

    times = [ int( time ) for time in times]
    distances = [ int( d ) for d in distances]

    return ( times, distances)

def computeWinningMargins( times, distances):

    nRaces = len( times )
    winningMargins = []

    for ii in range( nRaces ):

        t_ii = times[ii]
        d_ii = distances[ii]

        D = 0.5 * math.sqrt( t_ii * t_ii - 4 * d_ii )

        minTime = math.floor( 0.5 * t_ii - D + 1 )
        maxTime = math.ceil( 0.5 * t_ii + D - 1 )

        minTime = max( 0, minTime)
        maxTime = min( t_ii, maxTime)

        winningMargin = maxTime - minTime + 1
        winningMargins.append( winningMargin )

    return winningMargins