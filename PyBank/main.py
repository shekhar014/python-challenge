#import packages
import os
import csv

#open file
csvpath=os.path.join('Resources','03-Python_Homework_Instructions_PyBank_Resources_budget_data.csv')

#emply lists for month and revenue data
months = []
revenue = []

#read csv and parse data into lists
with open(csvpath, 'r') as csvfile:
    csvread = csv.reader(csvfile,delimiter=',')
    #skip header
    next(csvread, None)
    #parse data
    for row in csvread:
        months.append(row[0])
        revenue.append(int(row[1]))

#find total months
total_months = len(months)
#initialize
maxRevenue = revenue[0]
minRevenue = revenue[0]
netAmount = 0
revenue_change = revenue[0]
previousMonth = revenue[0]
sum_revenue_change = 0
for i in range(len(revenue)) :
    #Calculate revenue change between two months
    revenue_change = revenue[i] - previousMonth
    #Add Revenue Change for each month
    sum_revenue_change = sum_revenue_change + revenue_change
    #Comparision for max and min revenue
    if(revenue_change > maxRevenue):
        maxRevenue=revenue_change
        maxRevenuemonth = months[i] 
    elif(revenue_change < minRevenue):
        minRevenue = revenue_change
        minRevenuemonth = months[i]
    #Calculate Net Amount    
    netAmount = netAmount + revenue[i]
    #Update variable to store last month revenue
    previousMonth = revenue[i]
#calculate average_change
averagerevenueChange = round(sum_revenue_change/(total_months-1), 2)

#sets path for output file
output_dest = os.path.join('Output','pybank_output.txt')

# opens the output destination in write mode and prints the summary
with open(output_dest, 'w') as writefile:
    writefile.writelines('Financial Analysis\n')
    writefile.writelines('----------------------------' + '\n')
    writefile.writelines('Total Months: ' + str(total_months) + '\n')
    writefile.writelines('Total: $' + str(netAmount) + '\n')
    writefile.writelines('Average Change: $' + str(averagerevenueChange) + '\n')
    writefile.writelines('Greatest Increase in Profits: ' + maxRevenuemonth + ' ($' + str(maxRevenue) + ')'+ '\n')
    writefile.writelines('Greatest Decrease in Profits: ' + minRevenuemonth + ' ($' + str(minRevenue) + ')')

#opens the output file in r mode and prints to terminal
with open(output_dest, 'r') as readfile:
    print(readfile.read())
