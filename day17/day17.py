
import crucibles

file = open("./day17/data.txt")
lines = file.readlines()

heatLossMap = crucibles.parseHeatLossMap( lines )
optimalLossNormal = crucibles.optimizeHeatLoss( heatLossMap, lowerTurnLimit = 1, upperMoveLimit = 3)
optimalLossUltra = crucibles.optimizeHeatLoss( heatLossMap, lowerTurnLimit = 4, upperMoveLimit = 10)

print( optimalLossNormal )
print( optimalLossUltra )