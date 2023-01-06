#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv

with open("sample1.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
             print(row)


# In[ ]:




