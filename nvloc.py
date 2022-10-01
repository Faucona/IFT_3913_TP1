import os
import sys



# count the number of lines in java file
def nvloc(file):
	if(file.endswith('.java')):
			f = open(file)
			finalCount = lineCounter(f.readlines())
			f.close()

			return finalCount

# count the number of lines in given file
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


if __name__ == "__main__":
   out = nvloc(start(sys.argv[1]))
   print(out)






