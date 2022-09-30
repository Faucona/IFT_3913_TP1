import os
import sys
import pickle


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


if __name__ == "__main__":
   out = nvloc(start(sys.argv[1]))
   print(out)
   #return out 
#out = nvloc(start(sys.argv[1]))
#print(out)
# save output as out.pickle
#with open('nvloc_out.pickle', 'wb') as f:
	#pickle.dump(out, f)





