import re

input = open("4 input.txt", 'r')
lines = input.readlines()
keysList = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
keysPresent = {}
validPs = 0

def byr(value):
	try:
		return int(value) >= 1920 and int(value) <= 2002
	except ValueError as ex:
		return False

def iyr(value):
	try:
		return int(value) >= 2010 and int(value) <= 2020
	except ValueError as ex:
		return False

def eyr(value):
	try:
		return int(value) >= 2020 and int(value) <= 2030
	except ValueError as ex:
		return False

def hgt(value):
	unit = value[-2:]	
	try:
		if unit == "cm":	
			return int(value[0:3]) >= 150 and int(value[0:3]) <= 193
		elif unit == "in":
			return int(value[0:2]) >= 59 and int(value[0:2]) <= 76
		return False
	except ValueError as ex:
		return False

def hcl(value):
	pattern = re.compile("^[#]([0-9]|[a-f]){6}$")
	return pattern.match(value) is not None

def ecl(value):
	return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def pid(value):
	pattern = re.compile("^[0-9]{9}$")
	return pattern.match(value) is not None

switcher = {
	"byr": byr,
	"iyr": iyr,
	"eyr": eyr,
	"hgt": hgt,
	"hcl": hcl,
	"ecl": ecl,
	"pid": pid
}

def validateKey(key, value):
	validate = switcher.get(key)
	return validate(value)

def countKeys():
	for key in keysList:
		if key not in keysPresent:
			return 0
		if not validateKey(key, keysPresent[key]):
			print("invalid value ", keysPresent[key], " for key ", key)
			return 0
	return 1

for i in range(len(lines)):
	if lines[i] == "\n":
		print "blank"
		validPs += countKeys()
		keysPresent = {}
		continue
	print lines[i]
	pairs = lines[i].strip().split()
	for pair in pairs:
		pairList = pair.split(':')
		keysPresent[pairList[0]] = pairList[1]
validPs += countKeys()

print("" + str(validPs) + " valid passports")
