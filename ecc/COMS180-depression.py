print('------------------------------')
print('           RAW DATA           ')
print('------------------------------')

rawDataYears = [2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019]
rawDataCount = [2225000,2191000,1969000,2016000,2014000,1950000,1911000,2011000,2213000,2587000,2751000,3031000,3089000,3214000,3482000,3783000]
rawDataPercent = [9.0,8.8,7.9,8.2,8.3,8.1,8.0,8.2,9.1,10.7,11.4,12.5,12.8,13.3,14.4,15.7]
myRange = range(len(rawDataYears)) # myRange = range(16)

# Show raw data, in table format
def showRawData():
	print('Had incidence of MDE in past year:')
	print('Year | Count   | Percentage')
	for i in myRange:
		rDY = str(rawDataYears[i])
		rDC = str(rawDataCount[i])
		rDP = str(rawDataPercent[i])
		print(rDY + ' | ' + rDC + ' | ' + rDP + '%')
showRawData()

print('-------------------------------------')
print('           OBSERVED VALUES           ')
print('-------------------------------------')

# Invert rawDataCount: Count of youth that did not have incidence of MDE, rounded to nearest whole person
countInverse = [] # Initialize list of inverted counts (No counts)
for i in myRange: # 16 rows
	conversion = [int(round(rawDataCount[i] / rawDataPercent[i] * (100-rawDataPercent[i])))] # Yes count / Yes percentage * (100 - Yes percentage)
	countInverse += conversion # Add value to list of inverted counts
#print(countInverse)

# Combine two columns of data into one list of multiple rows
def formatIntoListOfRows(column1,column2): # Input two lists of column data
	listOfRows = [] # Initiliaze list of rows
	for i in myRange: # 16 rows
		aRow = [column1[i],column2[i]] # Combine i-th value from each column to obtain values for i-th row
		listOfRows.append(aRow) # Add values of i-th row to list of rows
	return(listOfRows) # Output list of rows
# Observed values, in list format (list of rows)
observed = formatIntoListOfRows(rawDataCount,countInverse)

# Calculate annual totals (sum each row)
def annualTotal(listOfValues): # Input list of values, i.e. observed
	annualTotal = [] # Initialize list of row totals, i.e. annual totals
	for i in range(len(listOfValues)): # 16 rows
		totalForOneYear = [sum(listOfValues[i])] # Total for one row
		annualTotal += totalForOneYear # Add row total to list of totals
	return(annualTotal) # Output list of row totals
# Totals for observed values
annualTotalsObserved = annualTotal(observed) # Observed values, list of totals for each row
yesNoTotalsObserved = [sum(rawDataCount),sum(countInverse)] # Observed values, list of totals for each column

# Show list of values, in table format
def showAsTable(valuesAsList):
	print('Had incidence of MDE in past year:')
	print('Year  | Yes     | No       | Total')
	yesTotal = 0
	noTotal = 0
	for i in myRange:
		year = rawDataYears[i]
		yesNo = []
		for j in range(2):
			yesNo += [valuesAsList[i][j]]
		annualTotal = sum(yesNo)
		print(str(year) + '  | ' + str(yesNo[0]) + ' | ' + str(yesNo[1]) + ' | ' + str(annualTotal))
		yesTotal += yesNo[0]
		noTotal += yesNo[1]
	grandTotal = yesTotal + noTotal
	print('Total | ' + str(yesTotal) + '| ' + str(noTotal) + '| ' + str(grandTotal))

# Show observed values, in table format
showAsTable(observed)

print('-------------------------------------')
print('           EXPECTED VALUES           ')
print('-------------------------------------')

"""
Formula: Expected[i][j] = Row[i] * Column[j] / N
"""

def calculateExpected(rowTotals,columnTotals): # Input marginal values from contingency table of observed values
	expected = [] # Initialize list of expected values
	grandTotal = float(sum(columnTotals)) # Convert from integer to float so that calculations are not rounded down by Python
	for i in range(len(rowTotals)): # 16 rows
		aRow = [] # Initialize list of values for each row, a [Yes count, No count] pair
		for j in range(len(columnTotals)): # 2 columns
			aRow += [rowTotals[i] * columnTotals[j] / grandTotal] # Add to list of values for each row
		expected.append(aRow) # Add row to list of expected values
	return(expected) # Output list of expected values
# Expected values, in list format (list of rows)
expected = calculateExpected(annualTotalsObserved,yesNoTotalsObserved)

# Show expected values, in table format
showAsTable(expected)

print('-------------------------------------')
print('           1. HYPOTHESES             ')
print('-------------------------------------')

print('H0: Incidence of MDE in youth is independent of the year.')
print('HA: Incidence of MDE in youth is related to the year.')

print('-------------------------------------')
print('         2. CRITICAL VALUE           ')
print('-------------------------------------')

# Chi square table source: https://www.mun.ca/biology/scarr/4250_Chi-square_critical_values.html
# Textbook only had first 10 rows. Source above matches textbook's first 10 rows.

dF = (len(rawDataYears)-1) * (2-1) # dF = 15
criticalValue = 24.996

print('df: ' + str(dF))
print('Signficance level: 0.05') # Assumed
print('Critical value: ' + str(criticalValue))

print('-------------------------------------')
print('         3. TEST STATISTIC           ')
print('-------------------------------------')

"""
Formula: X^2 = sum of (Observed - Expected)^2 / Expected
"""

testStats = [] # Initialize list of elements to sum
for i in myRange: # 16 rows
	for j in range(2): # 2 columns
		toSum = [((observed[i][j]-expected[i][j])**2)/expected[i][j]]
		testStats += toSum # Add value to list of elements to sum

testStatistic = sum(testStats) # Sum values, testStatistic = 19327.1640187
print('Test statistic: ' + str(testStatistic))

print('-------------------------------------')
print('            4. DECISION              ')
print('-------------------------------------')

if testStatistic > criticalValue:
	print('Test statistic > critical value.')
	print('Reject H0.')
else:
	print('Test statistic < critical value.')
	print('Fail to reject H0.')
# Reject H0.

print('-------------------------------------')
print('          5. EFFECT SIZE             ')
print('-------------------------------------')

"""
Formula: Cramer's V = sqrt( X^2 / N(k-1) )
"""

N = sum(yesNoTotalsObserved) # N = 85909662
k = min(len(yesNoTotalsObserved),len(annualTotalsObserved)) # k = 2
cramersV = (testStatistic/(N*(k-1)))**0.5 # cramersV = 0.0149990261038
print('Effect size: ' + str(cramersV))