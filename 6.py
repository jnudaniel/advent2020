input = open("6 input.txt", 'r')
lines = input.readlines()

totalSum = 0

yeses = set()
new = True

for lineStr in lines:
	line = lineStr.strip()
	print line
	if line == "":
		print(yeses)
		totalSum += len(yeses)
		yeses = set()
		new = True
		continue
	if new == True:
		for i in range(len(line)):
			yeses.add(line[i])
		new = False
	else:
		newYeses = set()
		for i in range(len(line)):
			newYeses.add(line[i])
		yeses = yeses.intersection(newYeses)


totalSum += len(yeses)
print totalSum


'''
for lineStr in lines:
	line = lineStr.strip()
	print line
	if line == "":
		print(yeses)
		totalSum += len(yeses)
		yeses = set()
	for i in range(len(line)):
		yeses.add(line[i])

totalSum += len(yeses)
print totalSum
'''