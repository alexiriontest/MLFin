# machine learning stock market predictions
import sys
import xlrd
# import plotly
# import numpy
# 
companies = []

class CompanyListing:
    
    def __init__(self, name):
      self.name = name
      self.quotes = []

    def getQuote(self, index):
        return self.quotes[index]

    def getNumPrices(self):
        return len(self.quotes)

    def addQuote(self, value):
        self.quotes.append(value)

    def avePrice(self):
        total = 0
        for index in range(len(self.quotes)):
            total += float(self.quotes[index])
        return str(total / 120)

    def getBeginEndDiff(self):
        return self.quotes[len(self.quotes)-1] - self.quotes[0]

inputFile = xlrd.open_workbook("workbook1.xlsx")
print("The number of sheets is {0}".format(inputFile.nsheets))
# print("Worksheet name(s): {0}".format(inputFile.sheet_names()))
dataGrid = inputFile.sheet_by_index(1)
print("Sheet ~{0}~ is: {1}x{2}".format(dataGrid.name, dataGrid.nrows, dataGrid.ncols))

for ry in range(dataGrid.ncols):
    curCompany = CompanyListing(dataGrid.cell_value(0, ry))
    companies.append(curCompany)
    for rx in range(dataGrid.nrows):
        if(rx != 0):
            curCompany.addQuote(dataGrid.cell_value(rx, ry))

for companyIndex in range(len(companies)):
    curCompany = companies[companyIndex]
    print(curCompany.name + " " + curCompany.avePrice())
    print("--->" + str(curCompany.getBeginEndDiff()))

