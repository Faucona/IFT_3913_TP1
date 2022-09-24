import os
import sys
import csv 


def jls(path):
	for file in os.listdir(path):

		result = os.path.join(path, file)
		if(file.endswith('.java')):

			f = open(result)
			strResult = ','.join(wordFinder(f.readlines()))

			f.close()

			strResult = f"{result}, {strResult}"
			tabResult = strResult.split(',') 
			tabValue.append(tabResult)


		elif os.path.isdir(result) :
			jls(result)
	return tabValue
def wordFinder(f):
	tabResult = []
	for line in f:
		if "package " in line and "*" not in line and '"' not in line:
			wordTab = line.split(" ")
			packageFound = wordTab[wordTab.index("package") + 1].replace(';','').replace('\n','')
			tabResult.append(packageFound)

		elif "class " in line and "*" not in line and '"' not in line:
			wordTab = line.split(" ")
			classFound = wordTab[wordTab.index("class") + 1]
			tabResult.append(classFound)
	return tabResult

def start(string):
	if (not isinstance(string, str)):
		return f"{string}"
	else:
		return string

tabValue = []

tab = jls(start(sys.argv[1]))

with open('jls.csv', 'w', newline='') as myfile:
     wr = csv.writer(myfile, delimiter=',')
     wr.writerows(tab)

print("Done")