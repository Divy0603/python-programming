a,b,c=map(int,input().split())
if(a>b and b>c) or (a>c and c>b):
   if(a):
      if(a>b and b>c):
         print(b)
      if(a>c and c>b):
         print(c)
elif(b>a and a>c) or (b>c and c>a):
   if(b):
      if(b>a and a>c):
         print(a)
      if(b>c and c>a):
         print(c)
elif(c>a and a>b) or (c>b and b>a):
   if(c):
      if(c>a and a>b):
         print(a)
      if(c>b and b>a):
         print(b)
