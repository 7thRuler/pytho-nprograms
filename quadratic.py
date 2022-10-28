#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("enter the coefficient of a quadratic equation")
a = int(input(print("a=")))
b = int(input(print("b=")))
c = int(input(print("c=")))
d = complex(b*b - 4*a*c)
s1 = (-b + d**0.5)/2*a
s2 = (-b - d**0.5)/2*a
print("the solutions of quadratic equation are ", s1,"and", s2)


# In[ ]:




