#!/usr/bin/env python
# coding: utf-8

# In[4]:


a=int(input("enter a number: "))
def fact(a):
    if a==1:
        return a
    else:
        return a*fact(a-1)
if a==0:
    print("factorial is 1")
elif a<0:
    print("factorial does not exist")
else:
    print("factorial is ",fact(a))

        
        
        
    
    


# In[ ]:




