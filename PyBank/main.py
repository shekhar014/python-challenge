#Import Required Package
import os
import csv

#Declaration and Initialization
file_path = "03-Python/Homework/Instructions/PyBank/Resources"
date = []
profit_losses = []
change_price = []
last_month_amount = 0
count = 1

#Read Data from the file
with open(os.path.join(file_path,"budget_data.csv"),mode ="r",encoding="utf-8",newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    #Skip Header
    next(csvreader,None)
    for row in csvreader:
        #Populate date and profit/losses list
        date.append(row[0])
        profit_losses.append(int(row[1]))
        #For first row skip calculating average change
        if(count==1):
            change_price.append(last_month_amount)
            last_month_amount = int(row[1])
            count = count + 1
        else:
        #From second row calculate average change between consecutive months    
            change_price.append((int(row[1])-last_month_amount))
            last_month_amount = int(row[1])
            count = count + 1

#Write to text file
with open(os.path.join(file_path,"PyBank.txt"),mode="w") as Pytxt:
    Pytxt.write("Financial Analysis\n")
    Pytxt.writelines("----------------------------\n")
    Pytxt.writelines(f"Total Months: {len(date)}\n")
    Pytxt.writelines(f'Total: ${sum(profit_losses)}\n')
    #Calculating average change in profit and losses
    Pytxt.writelines(f'Average Change: ${round(sum(change_price)/(len(change_price)-1),2)}\n')
    #Greatest Increase in profits
    Pytxt.writelines(f'Greatest Increase: {date[change_price.index(max(change_price))]} (${max(change_price)})\n')
    #Greatest Decrease in profits
    Pytxt.writelines(f'Greatest Decrease: {date[change_price.index(min(change_price))]} (${(min(change_price))})\n')

#Read from text file and print to console
with open(os.path.join(file_path,"PyBank.txt"),mode="r",newline="") as Pytxt:
    print(Pytxt.read())
    
