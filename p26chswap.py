#!/usr/bin/env python
# coding: utf-8

# In[1]:


def swap():
    str1=input("enter a word:")
    new=list(str1)
    first=new[0]
    last=new[-1]
    newstr=last+str1[1:-1]+first
    return newstr
print("new string is ",swap())


# In[ ]:




