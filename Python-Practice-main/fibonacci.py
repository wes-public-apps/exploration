# Wesley Murray
# 2/9/2021
# This script calculates X number of the fibonacci series.

#Inputs
seriesLength = 20
series = [0,1]

#Calculate Series
seriesStartLen =  len(series)
for i in range(seriesStartLen,seriesLength):
    series.append(series[i-seriesStartLen]+series[i+1-seriesStartLen])

#Display Result
print(series)
print("Value: "+str(series[seriesLength-1]))