#!/usr/bin/env python
# coding: utf-8

# In[15]:


a=int(input("enter the base:"))
n=int(input("enterthe limit:"))
s=1
print("Sum of exponetial series is")
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
for i in range(1,n):
    s=s+(a**i)/fact(i)
print(s)


    


# In[ ]:




