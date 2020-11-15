##kcharlesr

#import modules
import csv
import os

#csv path -- beginning in 'JHU_Git_Repo/Python' directory
csvpath = os.path.join('PyBank','Resources', 'budget_data.csv')

#read in csv file and skip header
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    #define variables and variable types
    month = []
    revenue = []
    revenue_change = []
         
    #create Loop to tally profits
    for row in csvreader:
        month.append(row[0])
        revenue.append(row[1])
   
    revenue_int = map(int,revenue)
    total_revenue = (sum(revenue_int))
    


    i = 0
    for i in range(len(revenue) - 1):
        profit_loss = int(revenue[i+1]) - int(revenue[i])
        revenue_change.append(profit_loss)
    sum_total = sum(revenue_change)
    monthly_change = sum_total / len(revenue_change)
    
    #define max, min and Month
    profit_increase = max(revenue_change)
    e = revenue_change.index(profit_increase)
    month_increase = month[e+1]
    profit_decrease = min(revenue_change)
    f = revenue_change.index(profit_decrease)
    month_decrease = month[f+1]


    #send summary results to terminal
    print('Financial Analysis')
    print('-' * 30)
    print(f'Total Months: {len(month)}')
    print(f'Total: ${total_revenue}')
    print('Average Change: $' + str(round(monthly_change, 2)))
    print(f"Greatest Increase in Profits: {month_increase} (${profit_increase})")
    print(f"Greatest Decrease in Profits: {month_decrease} (${profit_decrease})")

    #formatting and sending summary of results to summary text document
    results = os.path.join('PyBank', 'Analysis', 'Results.txt')
    with open(results, "w") as txt_file:
        txt_file.write('Financial Analysis' + '\n')
        txt_file.write('-' * 28 + '\n')
        txt_file.write(f'Total Months: {len(month)}\n')
        txt_file.write(f'Total: ${total_revenue}\n')
        txt_file.write('Average Change: $' + str(round(monthly_change, 2)) + '\n')
        txt_file.write(f'Greatest Increase in Profits: {month_increase} (${profit_increase})\n')
        txt_file.write(f'Greatest Decrease in Profits: {month_decrease} (${profit_decrease})\n')
