
import numpy as np

def parseHistories( lines ):

    oasisHistories = []

    for line in lines:

        historyII = np.fromstring( line, sep = " ")
        oasisHistories.append( historyII )

    return oasisHistories

def extrapolateHistories( histories ):
    
    extrapolations = []

    for history in histories:
        
        y = history[-1]

        changes = [y]
        dy = np.diff( history )

        while np.any( dy != 0 ):

            changes.append( dy[-1] )
            dy = np.diff( dy )

        extrapolation = np.cumsum( changes )
        extrapolation = int( extrapolation[-1] )

        extrapolations.append( extrapolation )

    return extrapolations