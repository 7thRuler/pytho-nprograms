def add(a,b):
  c=a+b 
  return c 
def sub(a,b): 
  d=a-b 
  return d
def mul(a,b): 
  e=a*b 
  return e 
def div(a,b): 
  f=a/b 
  return f

a=int(input("enter a number: "))
b=int(input("enter a number: "))
while(1):

  print("\n1.add\n2.diff\n3.mul\n4.div\n5.exit")
  x=int(input("enter youe choice: "))
  if x==1:
    print(add(a,b))
  elif x==2:
    print(sub(a,b))
  elif x==3:
    print(mul(a,b))
  elif x==4:
    print(div(a,b))
  elif x==5:
    break


