input = open("3 input.txt", 'r')
lines = input.readlines()

def sled(right, down):

	nTrees = 0
	#right = 3
	#down = 1
	x = 0
	tree = '#'
	i = 0

	#for i in range(6):#len(lines)):#6):
	while i < len(lines):
		line = lines[i].strip()
		#print(line, x)
		#print(x)
		if line[x] == tree:
			nTrees += 1
			#print("tree")
		if x + right >= len(line):
			x = (x + right) % len(line)
		else:
			x += right
		i += down
	print('trees: ', right, down, nTrees)
	return nTrees

print sled(1, 1) * sled(3, 1) * sled(5, 1) * sled(7, 1) * sled(1, 2)