#!/usr/bin/env python
# coding: utf-8

# In[602]:


# Import Pandas Library
import pandas as pd


# In[603]:


# Read the csv data
csvpath = r"PyPoll/Resources/PyPoll/Resources/election_data.csv"


# In[604]:


# create a dataframe to hold and analyze data
ed_df = pd.read_csv(csvpath)


# In[605]:


# Check to see if there are rows missing data
# ed_df.count()


# In[606]:


# create the data frame for by candidate

candidate_counts = ed_df["Candidate"].value_counts()
# candidate_counts


# In[607]:


# Convert the Candidate_Counts Series into a DataFrame
candidate_counts_df = pd.DataFrame(candidate_counts)
# candidate_counts_df.head()


# In[608]:


# Convert the column name into "Total Votes Won"
candidate_counts_df = candidate_counts_df.rename(
    columns={"Candidate": "Total Votes Won"})   
candidate_counts_df["Total Votes Won"] = candidate_counts_df["Total Votes Won"].map("({:.0f})".format)
candidate_counts_df.head()
candidate_counts_df.reset_index(inplace=True)
# candidate_counts_df.head()


# In[609]:


#Count Total Votes
totalv_count = ed_df['Voter ID'].count()
# totalv_count


# In[610]:


# Convert the Candidate_Counts / total votes Series into a DataFrame
candidate_per_df = round(pd.DataFrame(candidate_counts) / totalv_count * 100,2)
candidate_per_df = candidate_per_df.rename(
    columns={"Candidate": "Percent Votes Won"})
candidate_per_df.head()
candidate_per_df["Percent Votes Won"] = candidate_per_df["Percent Votes Won"].map("{:.3f}%".format)
candidate_per_df.reset_index(inplace=True)
# candidate_per_df.head()


# In[612]:


# Right Merge Candidate_Count_DF with Candidate_per_df on index
merge_vt_df = pd.merge(candidate_per_df, candidate_counts_df, on="index", how="right")
merge_vt_df = merge_vt_df.rename(
    columns={"index": "Candidate"})
# merge_vt_df.head()


# In[614]:


# use group by to create the percent of vote won and total votes
grouped_ed_df = ed_df.groupby(['Candidate'])
grouped_ed_df.count()
working_df = grouped_ed_df.count()
# working_df.count


# In[615]:


#create data set that totals the votes for each candidate
vote_count = ed_df["Candidate"].value_counts()
vote_count_df = pd.DataFrame(ed_df["Candidate"].value_counts())
# vote_count_df.columns


# In[616]:


# Create Election Analysis Summary
EA = ("Election Results")
dash = ("--------------------------------")
TV =  ("Total Votes: " + str(totalv_count))
# Dash
candidate1 = str(merge_vt_df.iloc[0,0] + ": " + merge_vt_df.iloc[0,1] + " " + merge_vt_df.iloc[0,2])
candidate2 = str(merge_vt_df.iloc[1,0] + ": " + merge_vt_df.iloc[1,1] + " " + merge_vt_df.iloc[1,2])
candidate3 = str(merge_vt_df.iloc[2,0] + ": " + merge_vt_df.iloc[2,1] + " " + merge_vt_df.iloc[2,2])
candidate4 = str(merge_vt_df.iloc[3,0] + ": " + merge_vt_df.iloc[3,1] + " " + merge_vt_df.iloc[3,2])
# Dash
winner = str("Winner: " + merge_vt_df.iloc[0,0])
# Dash

er_df = pd.DataFrame({"Election Results": [dash, TV, dash, 
candidate1, candidate2, candidate3, candidate4, dash, winner, dash],})

print(er_df)


# In[617]:


# Export a text file that contains the Election Results Text File
er_df.to_csv("PyPoll/Analysis/Election_Results.txt", index=False, header=True)

