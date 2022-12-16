#!/usr/bin/env python
# coding: utf-8

# In[2]:


stud={}
n=int(input("Enter No of Students : "))
for i in range(0,n):
    a=input("Enter Name:")
    stud[a]=int(input("Enter Mark :"))
print(stud)    
b=[]
b+=stud.keys()
b.sort()
for i in range(n):
    print(b[i],"\t\t\t",stud[b[i]])
 


# In[ ]:




