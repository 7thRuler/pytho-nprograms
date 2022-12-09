#!/usr/bin/env python
# coding: utf-8

# In[3]:


def re_fib(n):
    if n<=1:
        return n
    else:
        return re_fib(n-1)+re_fib(n-2)
a=int(input("enter the limt:"))
if a<=0:
    print("enter a positive integer")
else:
    print("The sequence is\n")
    for i in range(a):
        print(re_fib(i))

    


# In[ ]:




