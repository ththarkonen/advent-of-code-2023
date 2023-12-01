import common
import numpy as np

file = open("./day1/data.txt")
lines = file.readlines()

calibrationValues = common.parseDataPart1( lines )
calibrationValuesPart2 = common.parseDataPart2( lines )

totalCV = common.totalCalibrationValue( calibrationValues )
totalCV2 = common.totalCalibrationValue( calibrationValuesPart2 )

print( totalCV )
print( totalCV2 )