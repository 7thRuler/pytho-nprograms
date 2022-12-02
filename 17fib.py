#!/usr/bin/env python
# coding: utf-8

# In[7]:


a=int(input("limit of the fibanocci series "))
def fib(a):
    
    n1=0
    n2=1
    count=0
    if a<0:
        print("enter a positive number")
    elif a==0:
        print(n1)
    else:
        while count < a:
            print(n1)
            n3=n1+n2
            n1=n2
            n2=n3
            count+=1
fib(a)
        
    


# In[ ]:




