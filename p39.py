#!/usr/bin/env python
# coding: utf-8

# In[1]:


try: 
        fileptr = open("abc.txt","r")
        try: 
            fileptr.write("Hi I am good")
        finally: 
            fileptr.close() 
            print("file closed")
except: 
    print("Error")


# In[ ]:




