#!/usr/bin/env python
# coding: utf-8

# In[3]:


a=int(input("enter the base of exponental series: "))
b=int(input("enter the limit: "))
def exp(a,b):
    for i in range(0,b+1):
        print(a,"^",i,"=",a**i)
exp(a,b)
    


# In[ ]:




