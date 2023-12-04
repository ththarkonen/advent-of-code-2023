
import lottery

file = open("./day4/data.txt")
lines = file.readlines()

winningNumbers, lotteryNumbers = lottery.parseLotteryNumbers( lines )
points, matches = lottery.computePoints( lotteryNumbers, winningNumbers)
copyCards = lottery.copyCards( matches )

totalPoints = sum( points )
totalCards = sum( copyCards )

print( totalPoints )
print( totalCards )