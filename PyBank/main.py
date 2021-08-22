#!/usr/bin/env python
# coding: utf-8

# In[235]:


# import pandas libray
import pandas as pd


# In[246]:


# reac csv data and create in a dataframe
csvpath = r"PyBank\Resources\budget_data.csv"
bd_df = pd.read_csv(csvpath)


# In[238]:


# Create a Variable to hold count of months and create the test print statement for the analysis summary
month_count = bd_df['Date'].count()



# In[239]:


# Create Variable to hold total of Profit/Losses and create the test print statement for the anlysis summary
total_pl = bd_df["Profit/Losses"].sum()


# In[240]:


# Create a new column in the data frame to capture the change from the previous row to the next fow
bd_df["P&L Difference"] = bd_df["Profit/Losses"].diff()


# #create a new variable to hold the average/mean of all changes
plchg_mean = round(bd_df["P&L Difference"].mean(),2)


# In[241]:


# Determine the month with the greatest increase in profits and greatest decrease in profits
# Sort the dataframe by P&L Differnce smallest to largest
bd_dec_df = bd_df.sort_values("P&L Difference")


bd_dec_df['P&L Difference'] = bd_dec_df['P&L Difference'].fillna(0)
bd_dec_df['P&L Difference'] = bd_dec_df['P&L Difference'].astype(int)
# bd_dec_df.head

# # #reset index for the dataframe
bd_dec_df = bd_dec_df.reset_index(drop=True)
# bd_dec_df.head()



# # # # #capture date and largetest decrease
greatest_decrease_date = bd_dec_df.iloc[0,0]
greatest_decrease_amount = bd_dec_df.iloc[0,2]
print(greatest_decrease_date)
print(greatest_decrease_amount)
print("Greatest Decrease in Profits: " + greatest_decrease_date + " " + "($" + str(greatest_decrease_amount) + ")")


# In[242]:


# # ascending sort
# # Determine the month with the greatest increase in profits and greatest decrease in profits
# Sort the dataframe by P&L Differnce smallest to largest
bd_asc_df = bd_dec_df.sort_values("P&L Difference", ascending=False)


# # # #reset index for the dataframe
bd_asc_df = bd_asc_df.reset_index(drop=True)
# bd_asc_df.head()


# # # # #capture date and largetest decrease
greatest_increase_date = bd_asc_df.iloc[0,0]
greatest_increase_amount = bd_asc_df.iloc[0,2]
print(greatest_increase_date)
print(greatest_increase_amount)
print("Greatest Increase in Profits: " + greatest_increase_date + " " + "($" + str(greatest_increase_amount) + ")")


# In[248]:


# Create Financial Analysis Summary
FA = ("Financial Analysis")
dash = ("--------------------------------")
TM = ("Total Months: " + str(month_count))
T = ("Total: $" + str(total_pl))
AC = ("Average Change: $" + str(plchg_mean))
GI = ("Greatest Increase in Profits: " + greatest_increase_date + " " + "($" + str(greatest_increase_amount) + ")")
GD = ("Greatest Decrease in Profits: " + greatest_decrease_date + " " + "($" + str(greatest_decrease_amount) + ")")

fa_df = pd.DataFrame({
    "Financial Analysis": [dash, TM, T, AC, GI, GD],
    })

fa_df

print(fa_df)


# In[249]:


fa_df = pd.DataFrame({
    "Financial Analysis": [dash, TM, T, AC, GI, GD],
    })

fa_df


fa_df.to_csv("PyBank/Analysis/Financial_analysis.txt", index=False, header=True)

