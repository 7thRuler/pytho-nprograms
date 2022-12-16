
# In[7]:


def stradd():
    str1=input("enter your string:")
    a=len(str1)
    if a>2:
        if str1[-3:]=='ing':
            str1 += 'ly'
        else:
            str1 += 'ing'
    else:
        print("WORD IS TOO SMALL")
    return str1
print("updated strin is:",stradd())


# In[ ]:





# In[ ]:




