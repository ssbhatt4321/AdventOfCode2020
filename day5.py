import sys

seats = [int(l.replace('B','1').replace('R','1').replace('F','0').replace('L','0'), 2) for l in sys.stdin]
seats.sort()

#Part 1
print(seats[-1])

#Part 2
for i in range(seats[0], seats[-1]+1):
	if i not in seats:
		print(i)
