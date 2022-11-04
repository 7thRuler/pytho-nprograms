#!/usr/bin/env python
# coding: utf-8

# In[5]:


a=int(input("enter a number:"))
b=int(input("enter the second number:"))
print("MENU")
print("1.sum\n2.difference\n3.product\n4.quotient")
c=int(input("enter your choice(1/2/3/4):"))
if(c==1):
    print("sum of", a ,"and",b ,"is",a+b)
elif(c==2):
    print("difference of", a ,"and",b ,"is",a-b)
elif(c==3):
    print("product of", a ,"and",b ,"is",a*b)
elif(c==4):
    print("quotient of", a ,"and",b ,"is",a/b)
    
else:
    print("ivalid option")


# In[ ]:




