import csv
import sys
import nvloc
import math

tab = [] 
tab1 = []
tab2 = []

# open csv file
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
	# cast as int
	return int(elem)

# get the threshold from command line argument
threshold = math.ceil(int(sys.argv[1])/100 *len(tab))

tab1 = sorted(tab1,key=nvloc,reverse=True)
tab2 = sorted(tab2,key=lcsec,reverse=True)

temptab1 = [] 


for valueFound in tab1:
	if (len(temptab1) <threshold):
		value = valueFound
		temptab1.append(value)
temptab2 = [] 


for valueFound in tab2:
	if (len(temptab2) <threshold ):
		value = int(valueFound)
		temptab2.append(value)


# find the god classes
god_classes = []
counter = 0 
for row in tab:
	if(counter == threshold):
		break

	if (row[-1] in temptab1 and int(row[-2]) in temptab2):
		god_classes.append(row)
		counter += 1 

# write the god classes in a csv file
with open('egon.csv', 'w', newline='') as myfile:
     wr = csv.writer(myfile, delimiter=',')
     wr.writerows(god_classes)

for god_class in god_classes :
	print(god_class)
print("Done")

print(len(god_classes))
