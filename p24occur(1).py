#!/usr/bin/env python
# coding: utf-8

# In[13]:


l1 = []
n=int(input("enter the limit:"))
for i in range(n):
    ele=input()
    l1.append(ele)
    
ch=input("enter a character to find the occurance:")
def count(list1,n):
    c=0
    for i in list1:
        for j in i:
            if j==n:
                c=c+1
    return c

print("occurance is",count(l1,ch))
        
        


# In[ ]:





# In[ ]:




