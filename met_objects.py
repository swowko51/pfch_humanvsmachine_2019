import csv

#opening the MetObjects.csv to loop through
with open('MetObjects.csv', 'r') as met_csv:

	objects = csv.reader(met_csv)
	next(objects, None) #skips header
	count = 0

	# for row in objects:
	# 	print(row)


	#Pulling just the objects I want: 
	#Is Highlight = True, Public Domain = True, Classification = Paintings 
	for row in objects:
		if row[1] == 'True' and row[2] == 'True' and row[38] == 'Paintings':
			count = count + 1
			
			#Printing just the fields I want from the csv
			#Object Number and Tags
			print(row[0])
			print(row[6])
			print(row[40])
			print(row[43])
			print('+++++++++++++++++')


	print('---------------------')
	print(str(count))


