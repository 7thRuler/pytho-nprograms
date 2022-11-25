#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a=int(input("enter the starting point: "))
b=int(input("enter the finishing point: "))
print("primr numbers between",a,"and",b,"are")
for i in range(a,b+1):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i)

