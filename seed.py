_author_ = "Marcus"
import numpy
import csv
#from numpy import *
from random import *
# class data(object):
# 	def __init__(self,tag_,low_bound,up_bound,size):
# 		self.attr_A = []
# 		self.attr_B = []
# 		for i in range(0,size):
# 			self.attr_A.append(numpy.random.uniform(low_bound,up_bound))
# 			self.attr_B.append(numpy.random.uniform(low_bound,up_bound))
# 			if tag_ == 1:
# 				self.tag = 1
# 			else:
# 				self.tag = 0

def write_csv(size):
	csvfile = file('data_KNN&DT.csv','wb')
	writer = csv.writer(csvfile)
	data = []
	# for i in range(1000):
	# 	row = []
	# 	for j in range(size):
	# 		if j != 3 and j != 5 and j != 7:
	# 			row.append(numpy.random.uniform(0,10))
	# 		else:
	# 			if j == 3:
	# 				row.append(numpy.random.uniform(0.1,0.3))
	# 			elif j == 5:
	# 			   if row[3] < 0.2:
	# 			   		row.append(numpy.random.uniform(0.5,0.7))
	# 			   else:
	# 			  		row.append(numpy.random.uniform(0.4,0.6))
	# 			else:
	# 				if row[3] < 0.2 and row[5] > 0.6:
	# 					row.append(numpy.random.uniform(9,12))
	# 				elif row[3] < 0.2 and row[5] <= 0.6:
	# 					row.append(numpy.random.uniform(8,11))
	# 				else:
	# 					row.append(numpy.random.uniform(7,10))

	# 	if row[3] < 0.2 and row[5] > 0.6 and row[7] > 9.5:
	# 		row.append('A')
	# 	elif row[3] < 0.25 and row[5] < 0.6 and row[7] < 10:
	# 		row.append('B')
	# 	elif row[3] >= 0.25 and row[5] > 0.6 and row[7] < 9:
	# 		row.append('C')
	# 	elif row[3] >= 0.25 and row[5] < 0.45 and row[7] > 8.5:
	# 		row.append('D')
	# 	elif row[3] >= 0.2 and row[5] < 0.65 and row[7] < 8:
	# 		row.append('E')
	# 	elif row[3] < 0.2 and row[5] > 0.55 and row[7] > 10:
	# 		row.append('F')
	# 	elif row[3] < 0.2 and row[5] > 0.52 and row[7] > 8.6:
	# 		row.append('G')
	# 	elif row[3] >= 0.2 and row[5] > 0.5 and row[7] >= 10:
	# 		row.append('H')
	# 	elif row[3] >= 0.2 and row[5] > 0.45 and row[7] < 9:
	# 		row.append('I')
	# 	elif row[3] >= 0.2 and row[5] > 0.45 and row[7] >= 9:
	# 		row.append('K')
	# 	else:
	# 		row.append('M')
	# 	data.append(row)
	for i in range(1000):
		row = []
		for j in range(size):
			if j == 0:
				row.append(numpy.random.uniform(0.1,0.3))
			elif j == 1:
				if row[0] < 0.2:
				   	row.append(numpy.random.uniform(0.5,0.7))
				else:
				  	row.append(numpy.random.uniform(0.4,0.6))
			else:
				if row[0] < 0.2 and row[1] > 0.6:
					row.append(numpy.random.uniform(9,12))
				elif row[0] < 0.2 and row[1] <= 0.6:
					row.append(numpy.random.uniform(8,11))
				else:
					row.append(numpy.random.uniform(7,10))
		if row[0] < 0.2 and row[1] > 0.6 and row[2] > 9.5:
			row.append('A')
		elif row[0] < 0.25 and row[1] < 0.6 and row[2] < 10:
			row.append('B')
		elif row[0] >= 0.25 and row[1] > 0.6 and row[2] < 9:
			row.append('C')
		elif row[0] >= 0.25 and row[1] < 0.45 and row[2] > 8.5:
			row.append('D')
		elif row[0] >= 0.2 and row[1] < 0.65 and row[2] < 8:
			row.append('E')
		elif row[0] < 0.2 and row[1] > 0.55 and row[2] > 10:
			row.append('F')
		elif row[0] < 0.2 and row[1] > 0.52 and row[2] > 8.6:
			row.append('G')
		elif row[0] >= 0.2 and row[1] > 0.5 and row[2] >= 10:
			row.append('H')
		elif row[0] >= 0.2 and row[1] > 0.45 and row[2] < 9:
			row.append('I')
		elif row[0] >= 0.2 and row[1] > 0.45 and row[2] >= 9:
			row.append('K')
		else:
			row.append('M')
		data.append(row)			
	# for i in range(1000):
	# 	row = []
	# 	for j in range(size):
	# 		if j == 0:
	# 			row.append(numpy.random.uniform(0.1,0.3))
	# 		elif j == 1:
	# 			row.append(2*row[0])
	# 		elif j == 2:
	# 			row.append(3*row[1] - 0.2)
	# 	if row[0] < 0.2 and row[1] < 0.36 and row[2] < 0.85:
	# 		row.append('A')
	# 	elif row[1] >= 0.36 and row[2] > 0.9:
	# 		row.append('B')
	# 	elif row[0] > 0.2 and row[1] < 0.36 and row[2] > 0.85:
	# 		row.append('C')
	# 	else:
	# 		row.append('D')
	# 	data.append(row)

	name = []
	for i in range(size + 1):
		name.append(i)
	writer.writerow(name)
	for row in data:
		writer.writerow(row)
	csvfile.close()

#print row
# print data_1.attr_A[1]
write_csv(200)



