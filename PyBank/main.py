import os
import csv

# Path to collectio data from the Resources folder
budget_data = os.path.join("Resources","budget_data.csv")

print(budget_data)      

 # The total number of months included in the dataset (THESE ARE MY VARIABLES)                     
total_months = 0
total_pl = 0
value = 0
change = 0
date = []
profits = []
total = 0
net_change = 0
prev_net = 0
net_change_list = []
average_change = 0
greatest_increase = 0
greatest_increase_date = ""
greatest_decrease = 9999999999999999
greatest_decrease_date = ""



# Open and read the CSV File
with open(budget_data, "r") as csvfile:
   csvreader = csv.reader(csvfile, delimiter = ",")

#skip the header row
   next(csvreader, None)
   first_row = next(csvreader)
   total_months += 1
   total += int(first_row[1])
   prev_net = int(first_row[1]) 
  
    #loop through each row in the csv file
   for row in csvreader:

      #Extract the date and profit/loss value
      date = row[0]
      value = int(row[1])

      #total number of months
      total_months +=1 

      #net total amount of profit/losses over entire period
      total += int(row[1])


      #Add the change to the total change
      net_change = value - prev_net

      #Update the previous value
      prev_net = value

      #Calculate the average change in profit/loss value
      net_change_list += [net_change]

      #Greatest increase in profits (date and amount) over the entire period
      if net_change > greatest_increase:
         greatest_increase = net_change
         greatest_increase_date = date
      if net_change < greatest_decrease:
         greatest_decrease = net_change
         greatest_decrease_date = date   

#print results
print("total", total)

#Calculate the change in profit /loss
avg_net_change = sum(net_change_list) / len(net_change_list)        
print("total months:" + str(total_months))
print("total change: $" + str(net_change))
print("average change: $" + str(round(avg_net_change, 2)))
print("greatest increase in profits: " + greatest_increase_date + " ($" + str(greatest_increase) + ")")
print("greatest decrease in profits: " + greatest_decrease_date + " ($" + str(greatest_decrease) + ")")