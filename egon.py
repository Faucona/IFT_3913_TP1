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


# get the threshold
threshold = int(sys.argv[1])

# get the number of classes
num_classes = len(matrix)


# convert matrix to pandas dataframe

import pandas as pd
df = pd.DataFrame(matrix, columns = ['path', 'package', 'class', 'csec', 'nvloc'])
# cast column nvloc to float
df['nvloc'] = df['nvloc'].astype(float)
# cast column csec to float
df['csec'] = df['csec'].astype(float)


# get the nth % of the higher values of nvloc and csec
nvloc_threshold = df['nvloc'].quantile(1 - threshold/100)
csec_threshold = df['csec'].quantile(1 - threshold/100)

# find god classes
god_classes = df[(df['nvloc'] >= nvloc_threshold) & (df['csec'] >= csec_threshold)]['path'].tolist()

print(len(god_classes))

