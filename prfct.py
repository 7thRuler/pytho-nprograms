#!/usr/bin/env python
# coding: utf-8

# In[4]:


a=int(input("enter a number:"))
Sum=0
for i in range(1,a):
    if(a%i==0):
        Sum+=i
if Sum == a:
    print(a,"is perfect")
else:
    print(a,"is not perfect")
       
    


# In[ ]:




