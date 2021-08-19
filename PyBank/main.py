# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Read and store the data from the .csv file
data = open(r"C:\Users\benjy\Documents\Bootcamp Repos\python-challange\PyBank\Resources\budget_data.csv")
data = csv.reader(data)  
print(data)

data_header = next(data)

# print(data_header)
print(f"CSV Header: {data_header}")

# # Read each row of data after the header
for row in data:
    print(row)
    
# Identify total months in the data set
months = str(data[1])    
total_months = len(months)


    

    
