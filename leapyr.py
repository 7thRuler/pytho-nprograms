#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("enter a year to check leap year or not ")
a = int(input())
if(a%400 == 0):
    print(a, "is a leap year")
elif(a%4 ==0 and a%100 != 0):
    print(a, "is a leap year")


# In[ ]:




