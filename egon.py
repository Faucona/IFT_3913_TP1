import numpy as np
import csv
import sys
import os
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









# read lcsec.csv and put values in matrix and add nvloc values to matrix at the last column
with open('lcsec.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)
    matrix = np.array(data)
    # add colomn to matrix
    matrix = np.append(matrix, np.zeros((matrix.shape[0],1)), axis=1)
    # add nvloc values to matrix
    for i in range(matrix.shape[0]):
        matrix[i][4] = nvloc(matrix[i][0])

    
        

print(matrix)

# Utilisez le seuil de l’entée pour l’heuristique suivante : une classe est suspecte si ses métriques NVLOC et CSEC sont
# tous les deux dans les <seuil>% supérieures de toutes les classes dans le dossier et sous-dossiers.
# Par exemple, si le seuil est 10%, alors une classe est suspecte si ses métriques NVLOC et CSEC sont dans les 10% supérieures
# de toutes les classes dans le dossier et sous-dossiers.
#

# get the threshold
threshold = int(sys.argv[1])

# get the number of classes
num_classes = len(matrix)



