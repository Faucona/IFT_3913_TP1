import csv
import sys
import nvloc
import copy
import math

tab = [] 
tab1 = []
tab2 = []
with open('lcsec.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)
    for row in data:
    	if(len(row) == 4):
    		row.append(nvloc.nvloc(row[0]))
    		tab.append(row)
    		tab1.append(row[-1])
    		tab2.append(row[-2])


def nvloc(elem):
	return elem

def lcsec(elem):
	return int(elem)

threshold = math.ceil(int(sys.argv[1])/100 *len(tab))
print(threshold)
tab1 = sorted(tab1,key=nvloc,reverse=True)
tab2 = sorted(tab2,key=lcsec,reverse=True)

temptab1 = [] 
value = None

for valueFound in tab1:
	if ( (value == None or valueFound<value) and len(temptab1) <threshold):
		value = valueFound
		temptab1.append(value)
temptab2 = [] 
value = None
for valueFound in tab2:

	if ( (value == None or int(valueFound)<value) and len(temptab2) <threshold ):
		value = int(valueFound)
		temptab2.append(value)

god_classes = []
counter = 0 
for row in tab:
	if(counter == threshold):
		break

	if (row[-1] in temptab1 and int(row[-2]) in temptab2):
		god_classes.append(row)
		counter += 1 

with open('egon.csv', 'w', newline='') as myfile:
     wr = csv.writer(myfile, delimiter=',')
     wr.writerows(god_classes)

print("Done")
#print(len(god_classes))
