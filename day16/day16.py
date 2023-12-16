
import lasers
import time
from joblib import Parallel, delayed

file = open("./day16/data.txt")
lines = file.readlines()

components, nRows, nCols = lasers.parseComponents( lines )

start = time.time()
energized = lasers.trace( components, nRows, nCols, (0,0), (0,1))

nJobs = 60
job = Parallel( n_jobs = nJobs )
callback = delayed( lasers.trace )

call = lambda ii, jj, dir: callback( components, nRows, nCols, (ii,jj), dir)

rowInds = range( nRows )
colInds = range( nCols )

start = time.time()

leftEnergized  = job( call( ii, 0,         ( 0, 1)) for ii in rowInds )
rightEnergized = job( call( ii, nCols - 1, ( 0,-1)) for ii in rowInds )

topEnergized = job( call( 0, jj,         ( 1, 0)) for jj in colInds )
botEnergized = job( call( nRows - 1, jj, (-1, 0)) for jj in colInds )

stop= time.time()

optimalEnergized = max( leftEnergized + rightEnergized + topEnergized + botEnergized )

print( stop - start )
print( energized )
print( optimalEnergized )