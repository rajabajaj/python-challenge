import os
import csv


months_list = []
profits_loss = [] 

bank_path = os.path.join("..","Resources","budget_data.csv") 

with open(bank_path, newline = "") as bankfile:
    filereader = csv.reader(bankfile , delimiter=",")
    next(filereader) 
    for column in filereader:
        Date,ProfitLosses = column
        months_list.append(str(Date))
        profits_loss.append(int(ProfitLosses))
        net_profit = sum(profits_loss)
        total_months = len(months_list)
        
net_change = [y - x for x, y in zip(profits_loss[:-1], profits_loss[1:])]

def month_average(monthly_change):
    total = 0.0
    length = len(monthly_change)
    for num in monthly_change:
        total += float(num)
    return (total/length)        


greatest_incamt = int(max(profits_loss))
greatest_decamt = int(min(profits_loss))
list_maxmin = list(zip(profits_loss, months_list))

maximum_change = max(profits_loss) 
maximum_date = max(months_list)



minimum_change = min(profits_loss)
minimum_date = min(months_list)



print("FINANCIAL ANALYSIS")
print("----------------------------------------------")
print("Total Months : " + str(total_months))
print("Net Profit : " + str(net_profit))
print("Average Monthly Change :" + str(round(month_average(net_change))))
print("Greatest increase in profits : " + str(max(list_maxmin)[1]) , str(max(list_maxmin)[0]))
print("Greatest decrease in Losses : "  + str(min(list_maxmin)[1]) , str(min(list_maxmin)[0]))


FINAL RESULTS 

FINANCIAL ANALYSIS
----------------------------------------------
Total Months : 86
Net Profit : 38382578
Average Monthly Change :-2315
Greatest increase in profits : Feb-2012 1170593
Greatest decrease in Losses : Sep-2013 -1196225