import numpy as np

input = open("5 input.txt", 'r')
lines = input.readlines()

ROWMAX = 127
COLMAX = 7
seatIDs = np.zeros(948)

def getPlacement(axisStr, axisMax):
	low = 0
	hi = axisMax

	for i in range(len(axisStr)):
		char = axisStr[i]
		if char == 'F' or char == 'L':
			# update hi
			hi = (hi - low) / 2 + low
			#print("F - hi updated, range is", low, hi)
		elif char == 'B' or char == 'R':
			# update low
			low = (hi - low) / 2 + low + 1
			#print("B - low updated, range is", low, hi)
		else:
			print("Unexpected character", char)
			break
	#print(low, hi)
	return low

def getSeatID(line):
	rowStr = line[0:7]
	colStr = line[7:]
	return getPlacement(rowStr, ROWMAX) * 8 + getPlacement(colStr, COLMAX)

for line in lines:
	seatIDs[getSeatID(line.strip())] = 1

print seatIDs

print np.where(seatIDs == 0)

