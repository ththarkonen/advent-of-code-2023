
import springs
from joblib import Parallel, delayed

import time

file = open("./day12/data.txt")
lines = file.readlines()

symbols, altSymbols, numbers = springs.parse( lines )
symbolsFolded, altSymbolsFolded, numbersFolded = springs.fold( symbols, altSymbols, numbers)

sy = symbols
als = altSymbols
nu = numbers

sf = symbolsFolded
asf = altSymbolsFolded
nf = numbersFolded

nLines = len( lines )
inds = range( nLines )

nJobs = 30
job = Parallel( n_jobs = nJobs )
callback = delayed( springs.computePossibleCombinations )

callPart1 = lambda ii : callback( sy[ii], als[ii], nu[ii])
callPart2 = lambda ii : callback( sf[ii], asf[ii], nf[ii])

start = time.time()

nCombinations = job( callPart1(ii) for ii in inds )
nCombinationsFolded = job( callPart2(ii) for ii in inds )

stop = time.time()
print( stop - start )

totalPart1 = sum( nCombinations )

totalPart2 = 0
for result in nCombinationsFolded:
    totalPart2 = totalPart2 + result

print( totalPart1 )
print( totalPart2 )
