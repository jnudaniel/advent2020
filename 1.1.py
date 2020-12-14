import numpy as np

input = open("1.1 input.txt", 'r')
lines = input.readlines()
print(int(lines[0])-1)

'''
limit = 2020
half = limit / 2 + 1
inputs = np.zeros(half)


for line in lines:
	num = int(line)
	complement = 2020 - num
	if num < half:
		if inputs[num] == 2:
			print("num: ", num, " compl: ", complement, " product: ", num * complement)
			#break
		else:
			inputs[num] = 1
	else:	
		if inputs[complement] == 1:
			print("num: ", num, " compl: ", complement, " product: ", num * complement)
			#break
		else:
			inputs[complement] = 2
'''

limit = 2020
singles = []
doubles = np.zeros(limit + 1)

for line in lines:
	num = int(line)
	complement = limit - num
	# the two other numbers have been found
	if doubles[complement] != 0:
		first = doubles[complement]
		print("num: ", num, " first: ", first, " second: ", complement - first, " > product = ", num * first * (complement - first))
		#break
	else:
		# sum it to every existing number
		for single in singles:
			double = single + num
			if double < limit:
				doubles[single + num] = single
		# add that number to list
		singles.append(num)