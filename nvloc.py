import os
import sys


def nvloc(file):
	if(file.endswith('.java')):
			f = open(file)
			finalCount = lineCounter(f.readlines())
			f.close()

			return finalCount

def lineCounter(f):
	count = 0
	for line in f:
		if(line != "\n"):
			count+=1
	return count
def start(string):
	if (not isinstance(string, str)):
		return f"{string}"
	else:
		return string


print(nvloc(start(sys.argv[1])))
