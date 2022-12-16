#!/usr/bin/env python
# coding: utf-8

# In[12]:


n=int(input("Enter the number of students:"))
studlist=[]
for i in range(n):
    stud={}
    stud['Name']=input("Enter name:\n")
    stud["Branch"]=input("Enter branch:\n")
    stud["Roll no"]=int(input("Enter roll no:\n"))
    stud["mark"]=int(input("enter the mark:"))
    studlist.append(stud)
print("Name  Branch  Roll no mark")
print()
print()
for i in range(0,n):
    print(studlist[i]) 


# In[ ]:





# In[ ]:




