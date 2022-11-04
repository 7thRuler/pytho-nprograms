#!/usr/bin/env python
# coding: utf-8

# In[16]:


a = int(input("enter a three digit number:"))
Sum = 0
temp = a
while(temp>0):
        digit = temp % 10
        Sum += digit ** 3
        temp = temp / 10
        
if(Sum==temp):
    print(a,"is a armstrong number")
else:
    print(a,"is not a armstrong number")


# In[ ]:





# In[19]:


a = int(input("enter a three digit number:"))
Sum = 0
temp = a
while(temp>0):
        digit = temp % 10
        Sum += digit ** 3
        temp //= 10
        
if(Sum==a):
    print(a,"is a armstrong number")
else:
    print(a,"is not a armstrong number")


# In[ ]:




