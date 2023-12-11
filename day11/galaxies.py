
import numpy as np

def parse( lines, expansionRate):
    
    nRows = len( lines )
    nCols = len( lines[0] ) - 1

    galaxyMapDims = ( nRows, nCols)
    galaxyMapInitial = np.zeros( galaxyMapDims )

    for ii in range( nRows ):
        for jj in range( nCols ):

            marker_ii_jj = lines[ii][jj]
            if marker_ii_jj == "#": galaxyMapInitial[ii,jj] = 1

    emptyRowsBool = ~galaxyMapInitial.any( axis = 1 )
    emptyColsBool = ~galaxyMapInitial.any( axis = 0 )

    emptyRowInds = np.where( emptyRowsBool )
    emptyColInds = np.where( emptyColsBool )

    galaxyInds = np.where( galaxyMapInitial == 1 )
    galaxyRowInds = galaxyInds[0]
    galaxyColInds = galaxyInds[1]

    nGalaxies = len( galaxyRowInds )

    for ii in range( nGalaxies ):

        rowII = galaxyRowInds[ii]
        colII = galaxyColInds[ii]

        nRowPads = np.sum( emptyRowInds < rowII )
        nColPads = np.sum( emptyColInds < colII )

        galaxyRowInds[ii] = galaxyRowInds[ii] + ( expansionRate - 1 ) * nRowPads
        galaxyColInds[ii] = galaxyColInds[ii] + ( expansionRate - 1 ) * nColPads

    return galaxyRowInds, galaxyColInds

def computeDistances( galaxyIndsII, galaxyIndsJJ):

    distances = []
    nGalaxies = len( galaxyIndsII )

    for ii in range( nGalaxies ):
        for jj in range( ii + 1, nGalaxies ):

            x0 = galaxyIndsJJ[ii]
            x1 = galaxyIndsJJ[jj]

            y0 = galaxyIndsII[ii]
            y1 = galaxyIndsII[jj]
            
            L1_ii_jj = np.abs( x1 - x0 ) + np.abs( y1 - y0 )

            distances.append( L1_ii_jj )

    return distances