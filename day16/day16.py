
import lasers

import time
import json
from joblib import Parallel, delayed

file = open("./day16/data.txt")
lines = file.readlines()

components, nRows, nCols = lasers.parseComponents( lines )

start = time.time()
energized = lasers.trace( components, nRows, nCols, (0,0), (0,1))
nEnergizedPart1 = len( energized )

nJobs = 60
job = Parallel( n_jobs = nJobs )
callback = delayed( lasers.trace )

call = lambda ii, jj, dir: callback( components, nRows, nCols, (ii,jj), dir)

rowInds = range( nRows )
colInds = range( nCols )

start = time.time()

locationsLeft  = job( call( ii, 0,         ( 0, 1)) for ii in rowInds )
locationsRight = job( call( ii, nCols - 1, ( 0,-1)) for ii in rowInds )

locationsTop = job( call( 0, jj,         ( 1, 0)) for jj in colInds )
locationsBot = job( call( nRows - 1, jj, (-1, 0)) for jj in colInds )

stop= time.time()

locationsAll = locationsLeft + locationsRight + locationsTop + locationsBot
nEnergized = [ len(n) for n in locationsAll]
optimalEnergized = max( nEnergized )

with open( "./day16/lasers.json", "w") as f:
    json.dump( locationsAll, f)

print( stop - start )
print( nEnergizedPart1 )
print( optimalEnergized )
print( nRows, nCols )