import numpy as np
import csv
import sys
import os
import pickle




# load output from out.pickle
with open('nvloc_out.pickle', 'rb') as f:
    nvloc = pickle.load(f)




# read lcsec.csv and put values in matrix
with open('lcsec.csv', 'r', newline='') as myfile:
    csv_reader = csv.reader(myfile, delimiter=',')
    listcsv = list(csv_reader)
    matrix = np.array(listcsv)

print(matrix)






