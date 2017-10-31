# machine learning stock market predictions
import sys
import xlrd

inputFile = xlrd.open_workbook("workbook1.xlsx")
print("The number of sheets is {0}".format(inputFile.nsheets))
# print("Worksheet name(s): {0}".format(inputFile.sheet_names()))
dataGrid = file.sheet_by_index(1)
print("Sheet ~{0}~ is: {1}x{2}".format(sheetTwo.name, sheetTwo.nrows, sheetTwo.ncols))

for ry in range(sheetTwo.nrows):
	for rx in range(sheetTwo.ncols):
		if(rx == 0):
			print(sheetTwo.cell_value(rx, ry))
