def change(a,b):
    f1=str1[0]
    f2=str2[0]
    a=list(str1)
    b=list(str2)  
    a[0]=f2
    b[0]=f1
    s1="".join(a)
    s2="".join(b)
    s3=s1+" "+s2
    return s3
str1=input("enter a string")
str2=input("enter second string")
print("joined word is",change(str1,str2))
