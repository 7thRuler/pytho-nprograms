#!/usr/bin/env python
# coding: utf-8

# In[16]:


n=int(input("enter a number:"))

def pal(n):
    t=n
    r=0
    while n>0:
        p=n%10
        r=(r*10)+p
        n//=10
        
    if t==r:
        print(t,"is palindrome")
    else:
        print("not palindrome")
    
pal(n)    


# In[ ]:





# In[ ]:




