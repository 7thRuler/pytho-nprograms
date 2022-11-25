#!/usr/bin/env python
# coding: utf-8

# In[5]:


print("CONVERSION OF BINARY TO DECIMAL")
a=(input("enter your binary number: "))
n=len(a)
x=int(a)
def BtoD(x,n):
    temp=0
    for i in range(0,n):
        dec1=x%10
        temp+=dec1*(2**i)
        x//=10
    return temp
    
z=BtoD(x,n)
print("decimal=",z)


# In[ ]:




