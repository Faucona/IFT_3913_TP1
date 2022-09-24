import os
import sys
import csv 


def lcsec(*i):
	folder = i[0][0]
	csvFile = i[0][1]

	with open(csvFile, 'r', newline='') as myfile:
		csv_reader = csv.reader(myfile, delimiter=',')
		listcsv = list(csv_reader)
		for row in listcsv:
			if(len(row) == 3):
				f = open(row[0])
				finalCount = lineCounter(f.readlines(),row,listcsv)
				row.append(finalCount)
				f.close()

				tabValue.append(row)
	return tabValue

	

def lineCounter(f,crow,listcsv):
	count = 0
	for row in listcsv:
		if(len(row) >= 3 and row[2] != crow[2]):
			for line in f:
				if ( line.find(row[2]) != -1):
					count += 1

					break

	return count


def start(folder,csvFile):
	
	if (os.path.isfile(folder) and folder.endswith('.csv') and os.path.isdir(csvFile)):
		temp = folder
		folder = csvFile
		csvFile = temp 

		return folder,csvFile

	elif (os.path.isdir(folder) and os.path.isdir(csvFile)):
		print("an error occured both arguments are directories")

	elif(os.path.isfile(folder) and os.path.isfile(csvFile)):
		print("an error occured both arguments are files")

	else :
		return folder,csvFile
		
		

tabValue = []
tab = lcsec(start(sys.argv[1], sys.argv[2]))


with open('lsec.csv', 'w', newline='') as myfile:
     wr = csv.writer(myfile, delimiter=',')
     wr.writerows(tab)

print("Done")