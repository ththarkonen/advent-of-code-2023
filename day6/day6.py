
import boats

file = open("./day6/data.txt")
lines = file.readlines()

times, distances = boats.parseRaces( lines )
time, distance = boats.parseRace( lines )

winningMargins = boats.computeWinningMargins( times, distances)
winningMargins2 = boats.computeWinningMargins( time, distance)

total = 1
for margin in winningMargins:
    total = total * margin

print( winningMargins )
print( winningMargins2[0] )