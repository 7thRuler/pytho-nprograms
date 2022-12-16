#!/usr/bin/env python
# coding: utf-8

# In[2]:


def longestLength(a):
    max1 = len(a[0])
    temp = a[0]
    
    for i in a:
        if(len(i) > max1):
 
            max1 = len(i)
            temp = i
 
    print("The word with the longest length is:", temp,
          " and length is ", max1)
a=[]
n=int(input("enter the limit:"))
print("enter words:")
for i in range(n):
    ele=input()
    a.append(ele)
longestLength(a)


# In[ ]:




