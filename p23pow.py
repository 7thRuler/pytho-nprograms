#!/usr/bin/env python
# coding: utf-8

# In[11]:



def power(base,exp):
    s=1
    if exp==1:
        return base
    elif exp<0:
        exp=exp*(-1)
        s=s*(base*power(base,exp-1))
        return (1/s)
    elif exp>0:
        return base*power(base,exp-1)
    else:
        return 0
base=int(input("enter the base: "))
exp=int(input("enter the power value: "))
print(base,"^",exp,"=",power(base,exp))


# In[ ]:





# In[ ]:




