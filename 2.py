import numpy as np

def isValid1(line):
	tokens = line.split()
	bounds = tokens[0].split('-')
	minCt = int(bounds[0])
	maxCt = int(bounds[1])
	letter = tokens[1].strip(':')
	password = tokens[2]
	count = password.count(letter)
	if count >= minCt and count <= maxCt:
		return 1
	return 0

def isValid2(line):
	tokens = line.split()
	bounds = tokens[0].split('-')
	low = int(bounds[0]) - 1
	hi = int(bounds[1]) - 1
	letter = tokens[1].strip(':')
	password = tokens[2]

	#l = password[low] == letter
	#h = password[hi] == letter
	#print password, letter, low, l, hi, h
	if bool(password[low] == letter) != bool(password[hi] == letter):
		return 1
	return 0

input = open("2 input.txt", 'r')
lines = input.readlines()
nValid = 0

#for i in range(3):
for line in lines:
	#nValid += isValid1(line)
	nValid += isValid2(line)

print(nValid)