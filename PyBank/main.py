import os
import csv 

budget_csv = os.path.join('..','Resources', 'budget_data.csv')
text_file = "budget_summary.txt"

Total_Months = 0
Total_Revenue = 0
Previous_Revenue = 0
Revenue_Change = 0 
Revenue_Changes =[]
Revenue_Changes_Months =[]

with open(budget_csv, newline="") as file:
    csvreader = csv.reader(file, delimiter=",")

    csv_header = next(file)
    
    for row in csvreader:
        Total_Months +=1
        Total_Revenue += int(row[1])
        Revenue_Change = int(row[1]) - Previous_Revenue
        Previous_Revenue = int(row[1])
        Revenue_Changes.append(int(Revenue_Change))
        Revenue_Changes_Months.append(row[0])

Revenue_Changes = Revenue_Changes[1:]
Average_Change = sum(Revenue_Changes) / len(Revenue_Changes)
Greatest_Increase = max(Revenue_Changes)
Greatest_Increase_Month = Revenue_Changes_Months[Revenue_Changes.index(Greatest_Increase)+1]
Greatest_Decrease = min(Revenue_Changes)
Greatest_Decrease_Month = Revenue_Changes_Months[Revenue_Changes.index(Greatest_Decrease)+1]


print()
print()
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(Total_Months))
print("Total: " + "$" + str(Total_Revenue))
print("Average Change:" + "$" + str(round(Average_Change,2)))
print("Greatest Increase in Profits: " + str(Greatest_Increase_Month) + " ($" + str(Greatest_Increase) + ")")
print("Greatest Decrease in Profits: " + str(Greatest_Decrease_Month) + " ($" + str(Greatest_Decrease) + ")")
print()
print()


with open(text_file, "w") as txt_file:
    txt_file.write("Total Months: " + str(Total_Months))
    txt_file.write("\n")
    txt_file.write("Total: " + "$" + str(Total_Revenue))
    txt_file.write("\n")
    txt_file.write("Average Change:" + "$" + str(round(Average_Change,2)))
    txt_file.write("\n")
    txt_file.write("Greatest Increase in Profits: " + str(Greatest_Increase_Month) + " ($" + str(Greatest_Increase) + ")") 
    txt_file.write("\n")
    txt_file.write("Greatest Decrease in Profits: " + str(Greatest_Decrease_Month) + " ($" + str(Greatest_Decrease) + ")")

